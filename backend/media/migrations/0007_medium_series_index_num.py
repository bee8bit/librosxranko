# Generated by Django 3.2.8 on 2021-10-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20211021_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='medium',
            name='series_index_num',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Nummer innerhalb der Reihe'),
        ),
    ]
