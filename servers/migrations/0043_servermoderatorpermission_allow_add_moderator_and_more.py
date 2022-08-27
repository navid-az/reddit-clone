# Generated by Django 4.0.4 on 2022-08-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0042_servermoderatorpermission_allow_update_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='servermoderatorpermission',
            name='allow_add_moderator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servermoderatorpermission',
            name='allow_ban_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='servermoderatorpermission',
            name='allow_remove_user',
            field=models.BooleanField(default=False),
        ),
    ]
