from django.db.models import Q

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from django.shortcuts import get_object_or_404

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	UpdateAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

from .serializers import (
	PostCreateUpdateSerializer,
	PostDetailSerializer,
	PostListSerializer, 
	)

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	# permission_classes = [IsAuthenticated]


	# Save to logged in user
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	permission_classes = [IsOwnerOrReadOnly]


	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	permission_classes = [IsOwnerOrReadOnly]


class PostListAPIView(ListAPIView):
	#queryset = Post.objects.all()
	serializer_class = PostListSerializer
	filter_backends  = [SearchFilter, OrderingFilter]
	search_fields = ['title', 'content', 'user__first_name']
	pagination_class = PostPageNumberPagination#PageNumberPagination
	permission_classes = [AllowAny]
	lookup_field = 'slug'


	def get_queryset(self, *args, **kwargs):
		#queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = Post.objects.all() #filter(user=self.request.user)
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

		return queryset_list

from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView

class PostLikeAPIToggle(APIView):
	#authentication_classes 	= (authentication.SessionAuthentication,)
	permission_classes		= (permissions.IsAuthenticated,)

	def get(self, request, slug=None, format=None):
		# slug	= self.kwargs.get("slug")
		obj 	= get_object_or_404(Post, slug=slug)
		url_ 	= obj.get_api_url()
		user 	= self.request.user
		updated = False
		liked	= False
		if user.is_authenticated:
			if user in obj.likes.all():
				liked	= False
				obj.likes.remove(user)
			else:
				liked	= True
				obj.likes.add(user)
			updated = True
		data 	= {
			"updated":updated,
			"liked":liked
		}
		return Response(data)



