# Generated by Django 4.0.6 on 2022-08-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_remove_destination_video_destination_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='des1',
            field=models.TextField(default='no defined', null='True'),
            preserve_default='True',
        ),
    ]