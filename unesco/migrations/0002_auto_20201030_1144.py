# Generated by Django 3.1.1 on 2020-10-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
