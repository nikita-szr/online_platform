from rest_framework import serializers
from .models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'city', 'avatar']
        read_only_fields = ['email']