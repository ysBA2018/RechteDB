# Generated by Django 2.1 on 2018-08-18 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0008_auto_20180818_1317'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tbluseridundname',
            unique_together={('gruppe', 'geloescht'), ('userid', 'name', 'gruppe', 'orga', 'zi_organisation', 'geloescht'), ('gruppe', 'orga', 'zi_organisation', 'geloescht')},
        ),
    ]
