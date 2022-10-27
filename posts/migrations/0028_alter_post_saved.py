# Generated by Django 4.0.4 on 2022-10-02 10:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0027_rename_save_post_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='saved',
            field=models.ManyToManyField(blank=True, null=True, related_name='saves', to=settings.AUTH_USER_MODEL),
        ),
    ]