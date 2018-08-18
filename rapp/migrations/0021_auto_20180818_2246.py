# Generated by Django 2.1 on 2018-08-18 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapp', '0020_auto_20180818_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblgesamthistorie',
            name='modell',
            field=models.ForeignKey(db_column='Modell', on_delete=django.db.models.deletion.PROTECT, to='rapp.TblUebersichtAfGfs'),
        ),
        migrations.AlterField(
            model_name='tblgesamthistorie',
            name='plattform',
            field=models.ForeignKey(db_column='Plattform_ID', on_delete=django.db.models.deletion.PROTECT, to='rapp.TblPlattform'),
        ),
        migrations.AlterField(
            model_name='tblgesamthistorie',
            name='userid_name',
            field=models.ForeignKey(db_column='UserID + Name_ID', on_delete=django.db.models.deletion.PROTECT, to='rapp.TblUserIDundName'),
        ),
    ]