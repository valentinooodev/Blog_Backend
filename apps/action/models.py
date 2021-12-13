from django.db import models
from apps.blog.models import PostModel
from django.conf import settings


# Create your models here.

class UpvoteModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_upvote')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_upvote')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} - {self.post.title}'

    class Meta:
        verbose_name_plural = 'Upvotes'
        ordering = ('-created',)
        db_table = 'upvotes'


class CommentModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='post_comment')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id}: {self.post_id} - {self.content}'

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-created',)
        db_table = 'comments'
