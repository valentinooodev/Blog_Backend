from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'blog_api'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.PostListAPIView.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetailAPIView.as_view(), name='post_detail'),
]
