# Generated by Django 4.0.3 on 2022-03-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0024_alter_postphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
