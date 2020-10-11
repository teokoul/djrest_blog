from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
	model = Post

admin.site.register(Post, PostAdmin)
