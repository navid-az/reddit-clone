# Generated by Django 4.0.4 on 2022-06-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/header-pic/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/pic/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
