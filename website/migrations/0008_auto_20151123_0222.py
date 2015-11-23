# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20151123_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.CharField(max_length=200),
        ),
    ]
