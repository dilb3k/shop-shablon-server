from rest_framework import serializers
from .models import BlogModel
import uuid

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'start_data', 'end_data', 'image']

    def validate_image(self, value):
        if len(value.name) > 100:  # Fayl nomi 100 ta belgidan uzun bo‘lsa
            ext = value.name.split('.')[-1]
            value.name = f"{uuid.uuid4().hex[:10]}.{ext}"  # Yangi qisqa nom berish
        return value
