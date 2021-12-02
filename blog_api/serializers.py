from rest_framework import serializers
from blog import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'author', 'description', 'content', 'status')
        model = models.PostModel
