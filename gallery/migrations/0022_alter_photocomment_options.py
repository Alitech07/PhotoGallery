# Generated by Django 4.0.3 on 2022-03-25 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0021_alter_videocomment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocomment',
            options={'ordering': ('-date',)},
        ),
    ]
