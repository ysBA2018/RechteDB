# Generated by Django 2.1 on 2018-10-03 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0013_auto_20180915_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblgesamt',
            name='userid_name',
            field=models.ForeignKey(db_column='userid_und_name_id', on_delete=django.db.models.deletion.CASCADE, to='rapp.TblUserIDundName'),
        ),
        migrations.AlterField(
            model_name='tblrollehataf',
            name='einsatz',
            field=models.IntegerField(choices=[(0, 'nicht zugewiesen'), (1, 'Nur DV-User'), (2, 'XV, AV, BV, CV'), (4, 'nur XV-User'), (8, 'AV, BV, CV')], db_column='einsatz', default=0),
        ),
    ]
