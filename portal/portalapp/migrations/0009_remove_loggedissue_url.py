# Generated by Django 2.2.1 on 2019-05-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0008_auto_20190507_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggedissue',
            name='url',
        ),
    ]
