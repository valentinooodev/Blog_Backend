from django.urls import path
from . import views

app_name = 'action'

urlpatterns = [
    path('comment/create/', views.CreateComment.as_view(), name='create_comment'),
    path('comment/list/<str:pk>/', views.CommentList.as_view(), name='comment_list'),
    path('upvote/create/', views.CreateUpvote.as_view(), name='create_upvote'),
    path('upvote/delete/<int:pk>', views.DeleleUpvote.as_view(), name='delete_upvote'),

]
