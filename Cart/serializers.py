from rest_framework import serializers
from .models import CartModel

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = [
            'id', 'user_id', 'product_id', 'quantity', 'price', 'total_amount', 'order_date', 'status'  # ✅ `order_data` emas, `order_date`
        ]
