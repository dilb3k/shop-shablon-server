from rest_framework import serializers
from .models import OrderModel
from Usersapp.models import UserModel  
from Usersapp.serializers import UserSerializer  

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=True)
    
    class Meta:
        model = OrderModel
        fields = [
            'id', 
            'user', 
            'user_id', 
            'product_id', 
            'quantity', 
            'price', 
            'total_amount', 
            'order_date', 
            'status'
        ]
        extra_kwargs = {
            'order_date': {'read_only': True},
            'total_amount': {'read_only': True},
            'status': {'read_only': True}
        }
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
            
            # Total amountni hisoblaymiz
            validated_data['total_amount'] = validated_data['price'] * validated_data['quantity']
            
            order = OrderModel.objects.create(user=user, **validated_data)
            return order
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"user_id": "User does not exist!"})