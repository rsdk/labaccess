# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labaccess', '0003_labor_laborname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zugang',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('zugang_vname', models.CharField(verbose_name='Vorname', max_length=50)),
                ('zugang_nname', models.CharField(verbose_name='Nachname', max_length=50)),
                ('zugang_matnr', models.CharField(verbose_name='Matrikelnummer', max_length=5)),
                ('zugang_email', models.EmailField(max_length=254)),
                ('zugang_begruendung', models.CharField(verbose_name='Begründung', max_length=200)),
                ('zugang_anfrage_date', models.DateTimeField(verbose_name='Zugangsanfrage', auto_now_add=True)),
                ('zugang_genehmight_date', models.DateTimeField(editable=False, verbose_name='Genehmigung', null=True)),
                ('zugang_l', models.ForeignKey(to='labaccess.Labor')),
                ('zugang_v', models.ForeignKey(to='labaccess.Verantwortlicher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
