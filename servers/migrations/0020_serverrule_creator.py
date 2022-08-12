# Generated by Django 4.0.4 on 2022-08-12 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servers', '0019_serverusertag_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverrule',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rules', to=settings.AUTH_USER_MODEL),
        ),
    ]