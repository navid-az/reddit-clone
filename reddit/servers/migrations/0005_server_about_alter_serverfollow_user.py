# Generated by Django 4.0.4 on 2022-06-02 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servers', '0004_alter_server_tag_serverfollow'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='about',
            field=models.TextField(default='fasdf'),
        ),
        migrations.AlterField(
            model_name='serverfollow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_server', to=settings.AUTH_USER_MODEL),
        ),
    ]
