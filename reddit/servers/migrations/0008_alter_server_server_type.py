# Generated by Django 4.0.4 on 2022-07-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_remove_server_nsfw_alter_server_server_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(choices=[('pub', 'شخصی'), ('pri', 'عمومی')], max_length=3),
        ),
    ]