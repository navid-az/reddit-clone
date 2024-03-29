# Generated by Django 4.0.4 on 2022-08-18 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servers', '0023_alter_serverposttag_creator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_create_tag', models.BooleanField(default=True)),
                ('allow_create_rule', models.BooleanField(default=False)),
                ('allow_remove_user', models.BooleanField(default=True)),
                ('allow_remove_moderator', models.BooleanField(default=False)),
                ('allow_delete_post', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='moderators',
            field=models.ManyToManyField(related_name='moderators', to='servers.moderator'),
        ),
    ]
