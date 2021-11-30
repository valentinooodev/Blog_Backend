from django.contrib import admin
from . import models


@admin.register(models.CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostModel)
class PostModelAdmin(admin.ModelAdmin):
    pass
