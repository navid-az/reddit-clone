# Generated by Django 4.0.4 on 2022-06-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_alter_servertag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='about',
            field=models.TextField(default='about'),
        ),
    ]
