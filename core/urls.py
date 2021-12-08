from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Oath
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),

    # User Management
    path('api/v1/user/', include('users.urls', namespace='users')),

    # Blog API Application
    path('api/v1/', include('blog_api.urls', namespace='blog_api')),

    # API Schema & Docs
    path('docs/', include_docs_urls(title='PythonistaAPI')),
    path('schema/', get_schema_view(
        title='Pythonista Blog',
        description='API for Pythonista Blog',
        version='1.0.1'
    ),  name='openapi-schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
