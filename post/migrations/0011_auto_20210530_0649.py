# Generated by Django 3.1.7 on 2021-05-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20210530_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='og_image',
            field=models.FileField(null=True, upload_to='posts/ogFiles'),
        ),
    ]