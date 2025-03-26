from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# 🔹 Barcha foydalanuvchilarni olish va yangi foydalanuvchi qo'shish uchun
class UserListCreateAPI(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

# 🔹 ID bo'yicha bitta foydalanuvchini olish, o'zgartirish yoki o'chirish uchun
class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
