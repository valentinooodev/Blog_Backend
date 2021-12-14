from django.shortcuts import get_object_or_404
from apps.blog.models import PostModel, CategoryModel
from rest_framework.views import Response
from apps.action.models import CommentModel
from .serializers import PostSerializer, CategorySerializer
from rest_framework import filters, generics, permissions
from apps.commons.paginator import CustomPagination


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


# Display Posts
class PostList(generics.ListAPIView):
    pagination_class = CustomPagination
    serializer_class = PostSerializer
    queryset = PostModel.postobjects.all()


class PostListByCategory(generics.RetrieveAPIView):
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        item = self.kwargs.get('pk')
        posts = PostModel.postobjects.filter(category__slug=item)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


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
    permission_classes = [permissions.AllowAny]
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
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
