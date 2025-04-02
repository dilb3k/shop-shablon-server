from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import CartModel
from .serializers import CartSerializer
from rest_framework.views import APIView  
from rest_framework import status

# Barcha buyurtmalarni olish va yangi buyurtma qo'shish
class CartListCreateAPI(ListCreateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

# ID bo'yicha bitta buyurtmani olish, o'zgartirish yoki o‘chirish
class CartDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer
    
class ClearCartAPI(APIView):
    def delete(self, request):
        user = request.user
        # Delete all cart items for this user
        Cart.objects.filter(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)