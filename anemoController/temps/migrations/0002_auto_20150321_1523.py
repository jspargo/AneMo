# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settemp',
            old_name='set_temp',
            new_name='set_temp_high',
        ),
        migrations.AddField(
            model_name='settemp',
            name='set_temp_low',
            field=models.DecimalField(default=11.0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
