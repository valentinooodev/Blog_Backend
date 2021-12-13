from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Project URLs
    path('admin/', admin.site.urls),
    path('', include('apps.blog.urls', namespace='blog')),

    # Blog API Application
    path('api/v1/', include('apps.blog_api.urls', namespace='blog_api')),

    # API Schema & Docs
    path('docs/', include_docs_urls(title='PythonistaAPI')),
    path('schema/', get_schema_view(
        title='Pythonista Blog',
        description='API for Pythonista Blog',
        version='1.0.1'
    ),  name='openapi-schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
