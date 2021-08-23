# Generated by Django 3.2.6 on 2021-08-23 17:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_manager', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
