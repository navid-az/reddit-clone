# Generated by Django 4.0.4 on 2022-08-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0034_remove_servermoderator_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='servermoderator',
            name='server',
            field=models.ManyToManyField(blank=True, null=True, related_name='moderator_of', to='servers.server'),
        ),
    ]
