from rest_framework.viewsets import ModelViewSet
from api_shop.models import Product
from api_shop.serializers import ProductSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-created_at')
