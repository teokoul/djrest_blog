# Generated by Django 3.1 on 2020-08-31 18:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_like',
            field=models.ManyToManyField(blank=True, related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
