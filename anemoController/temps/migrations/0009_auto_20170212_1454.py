# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0008_auto_20170212_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordedtemp',
            options={'ordering': ['-recorded_date'], 'get_latest_by': 'recorded_date'},
        ),
        migrations.AlterModelOptions(
            name='settemp',
            options={'ordering': ['-set_date'], 'get_latest_by': 'set_date'},
        ),
    ]
