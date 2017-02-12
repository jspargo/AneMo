# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0005_auto_20170211_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempmanager',
            old_name='override',
            new_name='logic_state',
        ),
        migrations.RenameField(
            model_name='tempmanager',
            old_name='state',
            new_name='override_state',
        ),
    ]
