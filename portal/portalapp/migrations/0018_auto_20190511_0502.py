# Generated by Django 2.2.1 on 2019-05-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0017_student_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='handle',
            field=models.CharField(default=' ', max_length=25, unique=True),
        ),
    ]
