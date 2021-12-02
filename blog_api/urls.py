from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
#
# router.register('', views.PostList, basename='posts')
# router.register('', views.PostList, basename='user')
# urlpatterns = router.urls

urlpatterns = [

    path('', views.UserPostListAPIView.as_view(), name='user_post_list'),
    path('<str:pk>', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('search/', views.PostListAPIView.as_view(), name='post_list'),
    # Post admin
    path('admin/create/', views.CreatePost.as_view(), name='create_post'),
    path('admin/edit/postdetail/<int:pk>/', views.AdminPostDetail.as_view(), name='admin_detail_post'),
    path('admin/edit/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('admin/delete/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
]
