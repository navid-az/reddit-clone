# Generated by Django 4.0.4 on 2022-12-20 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0046_serverfollow_updated'),
        ('posts', '0053_alter_reportpost_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportpost',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='servers.server'),
        ),
    ]