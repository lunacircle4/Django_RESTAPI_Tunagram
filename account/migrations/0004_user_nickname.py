# Generated by Django 2.2.2 on 2019-07-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190702_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
    ]
