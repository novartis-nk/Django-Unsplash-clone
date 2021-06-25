# Generated by Django 3.1.7 on 2021-03-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tumbnail', models.ImageField(upload_to='posts/images')),
                ('Description', models.TextField(max_length=240)),
                ('camera', models.CharField(max_length=60)),
                ('photographer', models.CharField(max_length=60)),
                ('captured_time', models.DateField()),
                ('price', models.IntegerField()),
                ('pic_id', models.CharField(max_length=60)),
                ('tags', models.CharField(max_length=1000)),
            ],
        ),
    ]
