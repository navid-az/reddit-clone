# Generated by Django 4.0.4 on 2022-11-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0045_alter_server_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverfollow',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]