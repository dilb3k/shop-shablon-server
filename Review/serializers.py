from rest_framework import serializers
from .models import ReviewModel
from Usersapp.models import UserModel  




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=True)  # Make it required
    
    class Meta:
        model = ReviewModel
        fields = ['id', 'user', 'user_id', 'product_id', 'text', 'rating', 'data']
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        try:
            user = UserModel.objects.get(id=user_id)
            review = ReviewModel.objects.create(user=user, **validated_data)
            return review
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"user_id": "User does not exist!"})
        
        
        
