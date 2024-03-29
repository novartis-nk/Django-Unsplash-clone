# Generated by Django 3.1.7 on 2021-05-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210524_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='tumbnail',
        ),
        migrations.AddField(
            model_name='pic',
            name='og_image',
            field=models.FileField(default=0, null=True, upload_to='posts/ogFiles'),
        ),
        migrations.AddField(
            model_name='pic',
            name='preview',
            field=models.ImageField(default=0, upload_to='static/post/preview/'),
        ),
        migrations.AddField(
            model_name='pic',
            name='thumbnail',
            field=models.ImageField(default=0, upload_to='static/post/thumbnail/'),
        ),
    ]
