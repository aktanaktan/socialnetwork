from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from newtask_api import serializers
from newtask_api.models import Post, Like, DisLike
from newtask_api.serializers import UsersSerializer

from .permissions import IsOwnerOrReadOnly


class UserRegistationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UsersSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializers


class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )


class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializers
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializers


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DisLikeCreateView(generics.ListCreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = serializers.DisLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)