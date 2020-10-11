from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include("posts.api.urls", namespace='posts-api')),
    path('api/comments/', include("comments.api.urls", namespace='comments-api')),
    path('api/users/', include("accounts.api.urls", namespace='users-api')),
    path('api/profile/', include("profiles.api.urls", namespace='profiles-api')),

]