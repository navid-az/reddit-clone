# Generated by Django 4.0.4 on 2022-07-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='./static/user/img/default.jpg', null=True, upload_to='users/pic/'),
        ),
    ]
