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
    path('posts/', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('search/', views.PostListAPIView.as_view(), name='post_list'),
]
