# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20151122_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mes',
            name='ano',
            field=models.IntegerField(),
        ),
    ]
