from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product, ProductImage


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']


class ProductSerializer(ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.images.all()
        return [
            {
                'id': image.id,
                'url': request.build_absolute_uri(image.image.url),
                'alt_text': image.alt_text
            }
            for image in images
        ]


class ProductSearchSerializer(ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'discount_price',
            'stock', 'brand', 'category', 'images'
        ]

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.images.all()
        return [
            request.build_absolute_uri(image.image.url)
            for image in images
        ]
