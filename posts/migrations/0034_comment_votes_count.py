# Generated by Django 4.0.4 on 2022-11-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_rename_vote_postvote_comment_downvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='votes_count',
            field=models.IntegerField(default=0),
        ),
    ]
