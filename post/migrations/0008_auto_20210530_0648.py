# Generated by Django 3.1.7 on 2021-05-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20210530_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
