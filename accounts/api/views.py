from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

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
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

User = get_user_model()

from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer
	)

from posts.api.permissions import IsOwnerOrReadOnly
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	# queryset = User.objects.all()
	# permission_classes = [AllowAny]
	permission_classes = [AllowAny]

	def post(self, request, *args, **kwargs):
		serializer = UserCreateSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				new_data = serializer.data
				return Response(new_data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny]

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)

		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
	permissions_classes=(permissions.AllowAny,)

	def post(self, request):
		try:
			refresh_token = request.data["refresh_token"]
			token = RefreshToken(refresh_token)
			token.blacklist()
			return Response(status=status.HTTP_205_RESET_CONTENT)
		except Exception as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class HelloWorldView(APIView):

    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)

