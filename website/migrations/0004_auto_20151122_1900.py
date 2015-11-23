# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20151122_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ano',
            name='totalGastos',
            field=models.DecimalField(max_digits=14, decimal_places=2, default=0.0),
        ),
        migrations.AlterField(
            model_name='mes',
            name='totalGastos',
            field=models.DecimalField(max_digits=14, decimal_places=2, default=0.0),
        ),
    ]
