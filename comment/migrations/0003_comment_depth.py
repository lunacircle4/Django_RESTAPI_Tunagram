# Generated by Django 2.2.2 on 2019-07-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_parentcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='depth',
            field=models.IntegerField(default=0),
        ),
    ]
