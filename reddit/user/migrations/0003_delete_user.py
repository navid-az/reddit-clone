# Generated by Django 4.0.4 on 2022-06-02 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_karma'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]