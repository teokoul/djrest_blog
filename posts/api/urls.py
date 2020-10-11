from django.contrib import admin
from django.urls import path

from .views import (
	PostCreateAPIView,
	PostDeleteAPIView,
	PostUpdateAPIView,
	PostDetailAPIView,
	PostListAPIView,
	PostLikeAPIToggle
	)

app_name = "posts"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<slug>/', PostDetailAPIView.as_view(), name='detail'),
    path('<slug>/like/', PostLikeAPIToggle.as_view(), name='like-toggle'),
    path('<slug>/edit/', PostUpdateAPIView.as_view(), name='edit'),
    path('<slug>/delete/', PostDeleteAPIView.as_view(), name='delete'),
]
