# Generated by Django 4.0.4 on 2022-08-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0044_alter_server_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='image',
            field=models.ImageField(default='default/reddit.jpg', upload_to='servers/pic/'),
        ),
    ]