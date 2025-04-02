from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import OrderModel
from .serializers import OrderSerializer

# Barcha buyurtmalarni olish va yangi buyurtma qo'shish
class OrderListCreateAPI(ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

# ID bo'yicha bitta buyurtmani olish, o'zgartirish yoki o‘chirish
class OrderDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
