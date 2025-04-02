from rest_framework import serializers
from .models import Category, Subcategory

class SubcategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'category_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)

        # Bir xil category ichida slug bo‘lsa, xatolik qaytarish
        if Subcategory.objects.filter(category=category, slug=validated_data['slug']).exists():
            raise serializers.ValidationError({'slug': 'This slug already exists in this category'})

        return Subcategory.objects.create(category=category, **validated_data)


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image', 'subcategories']
