from rest_framework import serializers
from .models import CustomUser, Payment
from courses.models import Course, Lesson


class PaymentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    lesson = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_date', 'payment_method', 'course', 'lesson']


class UserProfileSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'city', 'avatar']
        read_only_fields = ['email']