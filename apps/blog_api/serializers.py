from rest_framework import serializers
from apps.blog.models import PostModel, CategoryModel
from apps.action.models import CommentModel
from apps.action.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'title', 'image', 'slug', 'author', 'description', 'content', 'status', 'view_count',
                  'comment_count', 'upvote_count')
        model = PostModel

    def get_comment_count(self, obj):
        cmts = obj.post_comment.all()
        result = len(list(cmts))
        return result

    def get_upvote_count(self, obj):
        upvotes = obj.post_upvote.all()
        return len(list(upvotes))


# class SeriesSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         fields = ('id', 'title', 'image', 'slug', 'author', 'description', 'content', 'status', 'view_count',
#                   'comment_count', 'upvote_count')
#         model = PostModel
#
#     def get_comment_count(self, obj):
#         cmts = obj.post_comment.all()
#         result = len(list(cmts))
#         return result
#
#     def get_upvote_count(self, obj):
#         upvotes = obj.post_upvote.all()
#         return len(list(upvotes))


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'slug', 'name', 'image')
        model = CategoryModel
