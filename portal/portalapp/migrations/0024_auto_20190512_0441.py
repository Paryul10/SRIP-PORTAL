# Generated by Django 2.2.1 on 2019-05-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0023_auto_20190511_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='handle',
            field=models.CharField(blank=True, default=None, max_length=25, null=True, unique=True),
        ),
    ]
