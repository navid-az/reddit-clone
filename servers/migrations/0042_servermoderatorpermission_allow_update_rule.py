# Generated by Django 4.0.4 on 2022-08-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0041_servermoderatorpermission_allow_delete_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='servermoderatorpermission',
            name='allow_update_rule',
            field=models.BooleanField(default=False),
        ),
    ]
