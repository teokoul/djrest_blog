from django.db import models
from django.conf import settings
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

# For unique slug
from django.db.models.signals import pre_save
from better.utils import unique_slug_generator

# Create your models here.
upload_location = "media/images/"

class Post(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title		= models.CharField(max_length=120)
	slug		= models.SlugField(blank=True, unique=True, editable=False)
	image		= models.ImageField(upload_to=upload_location,
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	likes		 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_like')
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	content 	 = models.TextField()
	draft		 = models.BooleanField(default=False)
	publish		 = models.DateField(auto_now=False, auto_now_add=False)
	read_time 	 = models.IntegerField(default=0)
	updated	  	 = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp 	 = models.DateTimeField(auto_now=False, auto_now_add=True)

	def get_api_url(self):
		return reverse("posts-api:detail", kwargs={"slug": self.slug})

	def get_like_url(self):
		return reverse("posts-api:like-toggle", kwargs={"slug": self.slug})

	# def get_likes_count(self):
	# 	return likes.count()

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

def post_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver, sender=Post)





