from django.db import models
from Usersapp.models import UserModel
from ProductApp.models import Product  # Product modelini import qilamiz


class LikeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # user_id emas, to'g'ri user FK
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # product_id ni to‘g‘ri FK qilish
    like_date = models.DateTimeField(auto_now_add=True)  # Like bosilgan vaqt

    def __str__(self):
        return f"Like: {self.user.username} -> {self.product.name}"
