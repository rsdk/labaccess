# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labaccess', '0004_zugang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labor',
            name='laborname',
            field=models.CharField(verbose_name='Laborname', max_length=200, default='wups', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verantwortlicher',
            name='firstname_text',
            field=models.CharField(verbose_name='Vorname', max_length=200, default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verantwortlicher',
            name='titel_text',
            field=models.CharField(verbose_name='Titel', max_length=200, default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zugang',
            name='zugang_anfrage_date',
            field=models.DateTimeField(verbose_name='Zugangsanfragen Datum'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='zugang',
            name='zugang_genehmight_date',
            field=models.DateTimeField(verbose_name='Genehmigung Datum', default='', blank=True),
            preserve_default=False,
        ),
    ]
