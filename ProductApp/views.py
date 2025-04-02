from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response  # ✅ Qo‘shildi
from rest_framework import status  # ✅ Qo‘shildi
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer

class ProductListCreateAPI(ListCreateAPIView):
    queryset = Product.objects.all().prefetch_related('images')
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

class ProductDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().prefetch_related('images')
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'id'

class ProductImageUploadAPI(CreateAPIView):
    serializer_class = ProductImageSerializer  # ✅ Qo‘shildi

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)  # ✅ O‘zgartirildi
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
