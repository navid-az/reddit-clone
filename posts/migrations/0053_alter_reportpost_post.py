# Generated by Django 4.0.4 on 2022-12-20 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0052_post_dates_alter_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
