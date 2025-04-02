from rest_framework import serializers
from django.contrib.auth import get_user_model

AdminUserModel = get_user_model()

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = AdminUserModel
        fields = ['id', 'username', 'phone', 'password']

    def create(self, validated_data):
        user = AdminUserModel(
            username=validated_data['username'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])  # Parolni hash qilish
        user.save()
        return user
