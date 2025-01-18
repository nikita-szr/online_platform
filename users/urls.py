from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentViewSet, UserRegistrationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('payments', PaymentViewSet, basename='payment')
router.register('register', UserRegistrationViewSet, basename='register')

urlpatterns = [
    path('profile/', UserViewSet.as_view({'get': 'profile'}), name='user-profile'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(router.urls)),
]
