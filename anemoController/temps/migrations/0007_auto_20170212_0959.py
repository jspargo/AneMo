# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0006_auto_20170211_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tempmanager',
            options={'get_latest_by': 'state_date'},
        ),
        migrations.RemoveField(
            model_name='tempmanager',
            name='recorded_temp',
        ),
    ]
