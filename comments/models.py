from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


# For unique slug
from django.db.models.signals import pre_save
from better.utils import unique_slug_generator

# Create your models here.

class CommentManager(models.Manager):
	def all(self):
		qs = super(CommentManager, self).filter(parent=None)
		return qs

	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
		return qs

	def create_by_model_type(self, model_type, slug, content, user, parent_obj=None):
		model_qs = ContentType.objects.filter(model=model_type)
		if model_qs.exists():
			SomeModel = model_qs.first().model_class()
			obj_qs = SomeModel.objects.filter(slug=slug)
			if obj_qs.exists() and obj_qs.count() == 1:
				instance = self.model()
				instance.content = content
				instance.user = user 
				instance.content_type = model_qs.first()
				instance.object_id = obj_qs.first().id
				if parent_obj:
					instance.parent = parent_obj
				instance.save()
				return instance
		return None



class Comment(models.Model):
	user			= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id		= models.PositiveIntegerField()
	content_object	= GenericForeignKey('content_type', 'object_id')
	parent			= models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
	comment_like	= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='comment_like')

	content 		= models.TextField()
	timestamp		= models.DateTimeField(auto_now_add=True)

	objects = CommentManager()

	def children(self):
		return Comment.objects.filter(parent=self)

	def get_api_url(self):
		return reverse("comments-api:thread", kwargs={"pk": self.pk})

	def get_comment_like_url(self):
		return reverse("comments-api:comment-like-toggle", kwargs={"pk": self.pk})

	# def get_content_type(self):
	# 	instance = self
	# 	content_type = ContentType.objects.get_for_model(instance.__class__)
	# 	return content_type

	@property
	def is_parent(self):
		if self.parent is not None:
			return False
		return True






	


	


