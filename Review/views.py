from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ReviewModel
from .serializers import ReviewSerializer

# Barcha buyurtmalarni olish va yangi buyurtma qo'shish
class CommentListCreateAPI(ListCreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

# ID bo'yicha bitta buyurtmani olish, o'zgartirish yoki o‘chirish
class CommentDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    
class ProductCommentsAPI(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ReviewModel.objects.filter(product_id=product_id).order_by('-data')

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            user=user,
            user_id=user.id,
            product_id=self.kwargs['product_id']
        )