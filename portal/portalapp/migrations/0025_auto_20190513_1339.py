# Generated by Django 2.2.1 on 2019-05-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0024_auto_20190512_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggedissue',
            name='issue_points',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='function_points',
            field=models.FloatField(default=0),
        ),
    ]
