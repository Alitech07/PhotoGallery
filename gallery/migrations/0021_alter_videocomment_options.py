# Generated by Django 4.0.3 on 2022-03-25 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0020_alter_videocomment_postvideo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videocomment',
            options={'ordering': ('-date',)},
        ),
    ]
