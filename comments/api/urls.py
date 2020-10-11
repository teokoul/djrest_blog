from django.contrib import admin
from django.urls import path

from .views import (
	CommentCreateAPIView,
	CommentDetailAPIView,
	CommentListAPIView,
	CommentLikeAPIToggle
	)

app_name = "comments"

urlpatterns = [
	path('', CommentListAPIView.as_view(), name='list'),
	path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<pk>/', CommentDetailAPIView.as_view(), name='thread'),
    path('<pk>/like/', CommentLikeAPIToggle.as_view(), name='comments-like-toggle'),
    #path('<id>/delete/', CommentListAPIView.as_view(), name='delete'),
]
