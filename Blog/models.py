import os
import uuid
from django.db import models

def rename_image(instance, filename):
    ext = filename.split('.')[-1]  # Fayl kengaytmasini olish (jpg, png)
    new_filename = f"{uuid.uuid4().hex[:10]}.{ext}"  # Tasodifiy 10 ta belgi bilan yangi nom
    return os.path.join('blog/', new_filename)  # "blog/" papkasiga yuklash

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    start_data = models.DateTimeField()
    end_data = models.DateTimeField()
    image = models.ImageField(upload_to=rename_image)  # Yangi yuklash funksiyasini qo‘shdik

    def __str__(self):
        return self.title
