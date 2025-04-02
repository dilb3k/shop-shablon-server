# views.py
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import LikeModel
from ProductApp.models import Product
from .serializers import LikeSerializer, ProductSerializer
from rest_framework.views import APIView

class LikeProductView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        liked_products = LikeModel.objects.filter(user=user).values_list('product_id', flat=True)
        products = Product.objects.filter(id__in=liked_products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product')
        
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        like, created = LikeModel.objects.get_or_create(
            user=request.user, 
            product_id=product_id
        )

        if created:
            return Response({"message": "Product liked successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Product already liked"}, status=status.HTTP_200_OK)

class LikeListCreateAPI(ListCreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        like, created = LikeModel.objects.get_or_create(user=request.user, product_id=product_id)

        if created:
            return Response({"message": "Product liked successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Product already liked"}, status=status.HTTP_200_OK)


class LikeDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UnlikeProductView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        product_id = self.kwargs.get('pk')
        return get_object_or_404(LikeModel, user=self.request.user, product_id=product_id)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Product unliked successfully"}, status=status.HTTP_200_OK)
