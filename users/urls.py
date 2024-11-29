from django.urls import path
from .views import UserProfileView, PaymentListView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
]