# Generated by Django 4.0.4 on 2022-08-24 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0037_remove_servermoderator_allow_create_rule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servermoderatorpermission',
            name='server',
        ),
    ]
