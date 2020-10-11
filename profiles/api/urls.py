from django.urls import path

from .views import (
    FollowingAPIToggle,
    profile_detail_api_view,
)
'''
CLIENT
Base ENDPOINT /api/profiles/
'''

app_name = "profiles"

urlpatterns = [
    path('<str:username>/', profile_detail_api_view, name='detail'),
    path('<str:username>/follow/', FollowingAPIToggle.as_view(), name='follow'),
]