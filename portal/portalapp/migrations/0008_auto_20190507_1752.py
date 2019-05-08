# Generated by Django 2.2.1 on 2019-05-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0007_loggedissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggedissue',
            name='url',
            field=models.URLField(default='https://github.com', unique=True),
        ),
        migrations.AlterField(
            model_name='loggedissue',
            name='commit_id',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]