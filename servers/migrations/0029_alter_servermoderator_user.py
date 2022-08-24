# Generated by Django 4.0.4 on 2022-08-20 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servers', '0028_remove_server_moderators_servermoderator_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servermoderator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderator_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
