# Generated by Django 2.2.1 on 2019-05-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0018_auto_20190511_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='handle',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
