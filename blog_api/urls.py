from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='list_post'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detail_post'),
    path('search/', PostListDetailfilter.as_view(), name='search_post'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='create_post'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admin_detail_post'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]
