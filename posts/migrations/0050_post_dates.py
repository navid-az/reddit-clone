# Generated by Django 4.0.4 on 2022-12-14 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0049_reportpost_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dates',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
