from django.contrib import admin
from django.urls import path

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	#ObtainTokenPairWithColorView,
	#CustomUserCreate,
	HelloWorldView,
	LogoutAndBlacklistRefreshTokenForUserView,
	)

from rest_framework_simplejwt import views as jwt_views


app_name = "comments"

urlpatterns = [
	path('login/', UserLoginAPIView.as_view(), name='login'),
	path('register/', UserCreateAPIView.as_view(), name='create_user'),

	path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
]
