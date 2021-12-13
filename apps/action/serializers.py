from rest_framework import serializers
from .models import UpvoteModel, CommentModel


class CreateUpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('post',)
        model = UpvoteModel


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user',)
        model = UpvoteModel


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('post', 'content')
        model = CommentModel


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        fields = ('user_name', 'content')
        model = CommentModel

    def get_user_name(self, obj):
        return obj.user.user_name
