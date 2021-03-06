from .views import PostList, PostDetail, PostListDetailFilter, CreatePost, EditPost, AdminPostDetail, DeletePost,\
    PostListByCategory, CategoryList
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'blog_api'

urlpatterns = [
    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Users URLs
    path('user/', include('apps.users.urls', namespace='user')),

    # Action URLs
    path('action/', include('apps.action.urls', namespace='action')),

    # Post URLs
    path('', PostList.as_view(), name='list_post'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detail_post'),
    path('search/', PostListDetailFilter.as_view(), name='search_post'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('category/<str:pk>/', PostListByCategory.as_view(), name='category_post'),


    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='create_post'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admin_detail_post'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

]
