from rest_framework import generics
from blog.models import CategoryModel, PostModel
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly


class PostUserWritePermission(BasePermission):
    message = 'Only author have permission to this post'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostListAPIView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = PostModel.postobjects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    # permission_classes = [PostUserWritePermission]
    queryset = PostModel.postobjects.all()
    serializer_class = PostSerializer
