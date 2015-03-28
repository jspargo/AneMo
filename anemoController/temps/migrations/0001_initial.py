# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recorded_temp', models.DecimalField(max_digits=5, decimal_places=2)),
                ('recorded_date', models.DateTimeField(verbose_name=b'date recorded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SetTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set_temp', models.DecimalField(max_digits=5, decimal_places=2)),
                ('set_date', models.DateTimeField(verbose_name=b'date set')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
