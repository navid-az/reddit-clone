# Generated by Django 4.0.4 on 2022-07-30 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0015_alter_server_header_image_alter_server_image'),
        ('posts', '0015_remove_save_is_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='servers.servertag'),
        ),
    ]
