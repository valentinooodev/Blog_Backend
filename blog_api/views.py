from rest_framework import generics, viewsets
from blog.models import CategoryModel, PostModel
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework.views import Response
from django.shortcuts import get_object_or_404


class PostUserWritePermission(BasePermission):
    message = 'Only author have permission to this post'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = PostModel.postobjects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     # permission_classes = [PostUserWritePermission]
#     queryset = PostModel.postobjects.all()
#     serializer_class = PostSerializer


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = PostModel.postobjects.all()
#
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = PostModel.postobjects.all()

    # def get_object(self, request=None, **kwargs):
    #     post = self.kwargs.get('pk')
    #     return get_object_or_404(PostModel, title=post)
    #
    # def get_queryset(self):
    #     return PostModel.objects.all()


