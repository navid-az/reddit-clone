# Generated by Django 4.0.4 on 2022-08-11 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_post_tag'),
        ('servers', '0016_alter_servertag_primary_color_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServerTag',
            new_name='ServerPostTag',
        ),
    ]