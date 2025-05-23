from rest_framework.viewsets import ModelViewSet , ViewSet
from rest_framework.response import Response
from api_shop.models import Product
from api_shop.serializers import ProductSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-created_at')




class ProductCategoryListView(ViewSet):

    def list(self , request):
        choices = [{'label': label} for key, label in Product.CATEGORY_CHOICES]

        return Response(choices)