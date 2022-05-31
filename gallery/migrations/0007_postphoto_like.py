# Generated by Django 4.0.3 on 2022-03-20 17:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0006_postphoto_author_postvideo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphoto',
            name='like',
            field=models.ManyToManyField(related_name='index', to=settings.AUTH_USER_MODEL),
        ),
    ]