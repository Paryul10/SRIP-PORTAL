# Generated by Django 2.2.1 on 2019-05-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0011_auto_20190507_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mentor',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
