from django.db import models
from Usersapp.models import UserModel  


class ReviewModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # Django User o‘rniga o‘z UserModelingiz
    product_id = models.CharField(max_length=10000)  
    text = models.CharField(max_length=244)  
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True)  
    data = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comment {self.id} - User {self.user.username}"
