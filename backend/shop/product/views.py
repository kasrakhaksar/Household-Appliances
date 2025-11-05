from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.cache import cache
from django_redis import get_redis_connection
from product.models import Product
from product.serializers import ProductSerializer, ProductSearchSerializer
import json


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.filter(
            is_active=True).order_by('-created_at')
        count = self.request.query_params.get('count')
        if count is not None:
            try:
                count = int(count)
                queryset = queryset[:count]
            except ValueError:
                pass
        return queryset

    def list(self, request, *args, **kwargs):
        redis_conn = get_redis_connection("default")
        cache_key = 'active_products_sorted_set'

        set_size = redis_conn.zcard(cache_key)
        if set_size > 0:
            cached_products = redis_conn.zrevrange(cache_key, 0, -1)
            serialized_products = [json.loads(item)
                                   for item in cached_products]
        else:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            serialized_products = serializer.data

            redis_conn.delete(cache_key)
            for product in serialized_products:
                created_at_timestamp = Product.objects.get(
                    id=product['id']).created_at.timestamp()
                redis_conn.zadd(
                    cache_key, {json.dumps(product): created_at_timestamp})
            redis_conn.expire(cache_key, 60 * 60)

        return Response(serialized_products)

    @action(detail=False, methods=['get'], url_path='categories')
    def categories(self, request):
        cache_key = 'product_category_choices'
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            choices = json.loads(cached_data)
        else:
            choices = [{'label': label, 'value': key}
                       for key, label in Product.CATEGORY_CHOICES]
            cache.set(cache_key, json.dumps(choices), 60 * 60)

        return Response(choices)

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        category_search = request.query_params.get('category', None)
        products = Product.objects.filter(
            is_active=True, category=category_search)
        serializer = ProductSearchSerializer(
            products, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='related')
    def related_products(self, request, pk=None):
        product = self.get_object()
        related = Product.objects.filter(
            category=product.category).exclude(id=product.id)[:5]
        serializer = self.get_serializer(related, many=True)
        return Response(serializer.data)
