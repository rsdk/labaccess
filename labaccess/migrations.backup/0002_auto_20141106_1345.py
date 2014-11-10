# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labaccess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verantwortlicher',
            name='firstname_text',
            field=models.CharField(verbose_name='Vorname', null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verantwortlicher',
            name='titel_text',
            field=models.CharField(verbose_name='Titel', null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='verantwortlicher',
            name='verantwortlicher_text',
            field=models.CharField(verbose_name='Nachname', max_length=200),
            preserve_default=True,
        ),
    ]
