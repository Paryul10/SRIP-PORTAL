# Generated by Django 2.2.1 on 2019-05-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_auto_20190507_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('commit_id', models.CharField(max_length=40)),
                ('issue_points', models.IntegerField(default=0)),
                ('is_added', models.BooleanField(default=False)),
            ],
        ),
    ]
