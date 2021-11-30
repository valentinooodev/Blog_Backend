from django.db import models
from commons.models import BaseModel
from django.conf import settings
from django.utils import timezone


class CategoryModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class PostModel(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    status_choice = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, default=1, related_name='post_category')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=status_choice, default='published')
    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-published',)
        db_table = 'post'

