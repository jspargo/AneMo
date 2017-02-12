# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0003_auto_20170211_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempmanager',
            name='recorded_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 11, 22, 6, 7, 458292, tzinfo=utc), verbose_name=b'date recorded'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='recorded_temp',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='set_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 11, 22, 6, 32, 54397, tzinfo=utc), verbose_name=b'date set'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='set_temp_high',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='set_temp_low',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
