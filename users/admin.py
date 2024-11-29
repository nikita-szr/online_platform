from django.contrib import admin

from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'course', 'lesson', 'amount', 'payment_method')
    list_filter = ('payment_method',)
