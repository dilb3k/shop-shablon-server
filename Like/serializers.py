from rest_framework import serializers
from .models import LikeModel
from ProductApp.models import Product
from ProductApp.serializers import ProductSerializer

class LikeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = LikeModel
        fields = ['id', 'user', 'product', 'product_id', 'like_date']
        read_only_fields = ['user']  # `user`ni avtomatik olish uchun

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user  # User avtomatik qo‘shiladi
        product_id = validated_data.pop('product_id')
        product = Product.objects.get(id=product_id)
        return LikeModel.objects.create(product=product, **validated_data)
