# Generated by Django 4.0.3 on 2022-03-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_alter_photocomment_date_alter_videocomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='videocomment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]