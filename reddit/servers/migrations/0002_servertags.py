# Generated by Django 4.0.4 on 2022-06-08 13:26

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('primary_color', colorfield.fields.ColorField(default='#ffff', image_field=None, max_length=18, samples=None)),
                ('secondary_color', colorfield.fields.ColorField(default='#ffff', image_field=None, max_length=18, samples=None)),
                ('is_allowed', models.BooleanField(default=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='servers.server')),
            ],
        ),
    ]
