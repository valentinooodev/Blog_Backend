from django.urls import path
from . import views

app_name = 'action'

urlpatterns = [
    path('comment/create/', views.CreateComment.as_view(), name='create_comment'),
    path('comment/list/<int:pk>/', views.CommentList.as_view(), name='comment_list'),
]
