# Generated by Django 4.0.4 on 2022-10-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_alter_post_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
