from django.db import models
from commons.models import BaseModel
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


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
    image = models.ImageField(_('Image'), upload_to=upload_to, default='posts/default.jpg')
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


class SeriesModel(models.Model):
    status_choice = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='series_author')
    image = models.ImageField(_('Image'), upload_to=upload_to, default='posts/default.jpg')
    description = models.TextField(null=True)
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    status = models.CharField(max_length=15, choices=status_choice, default='published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ('-published',)
        db_table = 'series'


class SubPostModel(models.Model):
    status_choice = (
        ('published', 'Published'),
        ('draft', 'Draft'),
    )

    title = models.CharField(max_length=255)
    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE, related_name='series_author')
    slug = models.SlugField(max_length=250, unique_for_date='published')
    status = models.CharField(max_length=15, choices=status_choice, default='published')
    index = models.IntegerField(default=1)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Posts'
        ordering = ('index',)
        db_table = 'sub_posts'
