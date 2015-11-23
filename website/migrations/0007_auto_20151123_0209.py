# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_datafile_active'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='funcionario',
            unique_together=set([]),
        ),
    ]
