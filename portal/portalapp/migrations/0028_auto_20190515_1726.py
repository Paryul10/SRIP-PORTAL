# Generated by Django 2.2.1 on 2019-05-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0027_loggedissue_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedissue',
            name='handle',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
