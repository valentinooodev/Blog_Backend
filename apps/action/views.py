from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import Response
from .serializers import UpvoteSerializer, CommentSerializer, CreateUpvoteSerializer, CreateCommentSerializer
from .models import UpvoteModel, CommentModel


class CreateUpvote(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpvoteSerializer
    queryset = UpvoteModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateComment(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateCommentSerializer
    queryset = CommentModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
    queryset = CommentModel.objects.all()

    def get(self, request, *args, **kwargs):
        item = self.kwargs.get('pk')
        cmts = CommentModel.objects.filter(post_id=item)
        serializer = CommentSerializer(cmts, many=True)
        return Response(serializer.data)


class Upvote(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = UpvoteModel.objects.all()
