from rest_framework.viewsets import ModelViewSet , ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from api_shop.models import Product
from api_shop.serializers import ProductSerializer
from django.core.cache import cache
from django_redis import get_redis_connection
import json







class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-created_at')

    def list(self, request, *args, **kwargs):
        redis_conn = get_redis_connection("default")
        cache_key = 'active_products_sorted_set'

        set_size = redis_conn.zcard(cache_key)
        if set_size > 0:
            print("Cache hit: using sorted_set from Redis.")
            cached_products = redis_conn.zrevrange(cache_key, 0, -1)
            serialized_products = [json.loads(item) for item in cached_products]
        else:
            print("Cache miss: querying database and populating sorted_set.")
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            serialized_products = serializer.data

            redis_conn.delete(cache_key)

            for product in serialized_products:
                created_at_timestamp = (
                    Product.objects.get(id=product['id']).created_at.timestamp()
                )
                redis_conn.zadd(
                    cache_key,
                    {json.dumps(product): created_at_timestamp}
                )

            redis_conn.expire(cache_key, 60 * 60)

        return Response(serialized_products)





class ProductCategoryListView(ViewSet):

    def list(self, request):
        cache_key = 'product_category_choices'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            print("Cache hit: using cached category choices.")
            choices = json.loads(cached_data)
        else:
            print("Cache miss: serializing category choices.")
            choices = [{'label': label} for key, label in Product.CATEGORY_CHOICES]
            cache.set(cache_key, json.dumps(choices), 60 * 60)

        return Response(choices)






class SignupView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not name or not email or not password:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=email).exists():
            return Response({'error': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=name,
            password=password
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)