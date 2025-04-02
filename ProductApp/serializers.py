from rest_framework import serializers
from .models import Product, ProductImage, Category, Subcategory

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), source='subcategory', write_only=True
    )

    category = serializers.IntegerField(source='category.id', read_only=True)
    subcategory = serializers.IntegerField(source='subcategory.id', read_only=True)

    images = ProductImageSerializer(many=True, required=False)  # Rasmlarni olish uchun
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'short_description', 'price',
            'category_id', 'subcategory_id', 'category', 'subcategory', 'images',
            'inStock', 'rating', 'updated_at', 'created_at'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        instance = super().update(instance, validated_data)

        if images_data:
            instance.images.all().delete()  # Eski rasmlarni o‘chirib yangi rasmlar qo‘shiladi
            for image_data in images_data:
                ProductImage.objects.create(product=instance, **image_data)
        
        return instance
