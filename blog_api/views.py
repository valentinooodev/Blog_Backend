from rest_framework import generics, viewsets
from blog.models import CategoryModel, PostModel
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, \
    IsAuthenticated, AllowAny
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class PostUserWritePermission(BasePermission):
    message = 'Only author have permission to this post'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class UserPostListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return PostModel.objects.filter(author=user)


class PostDetailAPIView(generics.ListAPIView):
    # permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print('slug: ', slug)
        return PostModel.objects.filter(slug=slug)


class PostListAPIView(generics.ListAPIView):
    queryset = PostModel.postobjects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


class PostSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']

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

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer
#     queryset = PostModel.postobjects.all()

# def get_object(self, request=None, **kwargs):
#     post = self.kwargs.get('pk')
#     return get_object_or_404(PostModel, title=post)
#
# def get_queryset(self):
#     return PostModel.objects.all()
