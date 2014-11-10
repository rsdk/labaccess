# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labaccess', '0005_auto_20141110_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zugang',
            name='zugang_genehmight_date',
            field=models.DateTimeField(verbose_name='Genehmigung Datum', null=True),
            preserve_default=True,
        ),
    ]
