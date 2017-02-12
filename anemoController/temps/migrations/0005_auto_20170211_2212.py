# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0004_auto_20170211_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempmanager',
            name='recorded_date',
        ),
        migrations.RemoveField(
            model_name='tempmanager',
            name='set_date',
        ),
        migrations.RemoveField(
            model_name='tempmanager',
            name='set_temp_high',
        ),
        migrations.RemoveField(
            model_name='tempmanager',
            name='set_temp_low',
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='override',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='state',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tempmanager',
            name='state_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 11, 22, 12, 54, 406220, tzinfo=utc), verbose_name=b'state date'),
            preserve_default=False,
        ),
    ]
