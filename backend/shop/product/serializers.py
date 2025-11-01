from rest_framework.serializers import ModelSerializer , SerializerMethodField
from .models import Product



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductSearchSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'discount_price',
            'stock', 'brand', 'category', 'image'
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None