# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('dataFile', models.FileField(upload_to='dataFiles/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='datafile',
            unique_together=set([('mes', 'ano')]),
        ),
    ]
