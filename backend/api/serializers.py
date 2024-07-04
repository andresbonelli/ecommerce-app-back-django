from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Producto

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["name", "description", "storage", "carbs", "fat", "protein", "salt", "price", "stock", "image"]