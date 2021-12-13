from django.shortcuts import get_object_or_404
from apps.blog.models import PostModel, CategoryModel
from apps.action.models import CommentModel
from .serializers import PostSerializer, CategorySerializer
from rest_framework import filters, generics, permissions


# Display Posts
class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class PostListByCategory(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        result = get_object_or_404(CategoryModel, slug=item)
        return result


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        result = get_object_or_404(PostModel, slug=item)
        try:
            result.view_count += 1
            result.save()
        except:
            pass
        return result


# Post Search
class PostListDetailFilter(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# Post Admin

class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
