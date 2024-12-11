from rest_framework import serializers
from .models import CustomUser, Payment
from courses.models import Course, Lesson


class PaymentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    lesson = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'city', 'avatar']
        read_only_fields = ['email']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'is_staff']
        read_only_fields = ['id', 'is_staff', 'email']
