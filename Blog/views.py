from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# 🔹 Barcha foydalanuvchilarni olish va yangi foydalanuvchi qo'shish uchun
class BlogListCreateAPI(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    parser_classes = [MultiPartParser, FormParser]
    

# 🔹 ID bo'yicha bitta foydalanuvchini olish, o'zgartirish yoki o'chirish uchun
class BlogDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
