# Generated by Django 4.0.4 on 2022-06-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
