# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20151122_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafile',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
