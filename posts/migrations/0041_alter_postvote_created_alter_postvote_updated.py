# Generated by Django 4.0.4 on 2022-11-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0040_alter_post_created_alter_post_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvote',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='postvote',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]