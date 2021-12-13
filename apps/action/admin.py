from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.UpvoteModel)
class PostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommentModel)
class PostModelAdmin(admin.ModelAdmin):
    pass
