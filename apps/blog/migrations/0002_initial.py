# Generated by Django 3.2.9 on 2021-12-12 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='post_category', to='blog.categorymodel'),
        ),
    ]