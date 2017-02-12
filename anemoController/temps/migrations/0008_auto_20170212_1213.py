# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0007_auto_20170212_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settemp',
            options={'get_latest_by': 'set_date'},
        ),
        migrations.AlterModelOptions(
            name='tempmanager',
            options={'ordering': ['-state_date']},
        ),
    ]
