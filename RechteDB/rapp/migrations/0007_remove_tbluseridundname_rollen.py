# Generated by Django 2.1 on 2018-09-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0006_auto_20180909_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbluseridundname',
            name='rollen',
        ),
    ]
