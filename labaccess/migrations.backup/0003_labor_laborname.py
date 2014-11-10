# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labaccess', '0002_auto_20141106_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='laborname',
            field=models.CharField(verbose_name='Laborname', max_length=200, null=True),
            preserve_default=True,
        ),
    ]
