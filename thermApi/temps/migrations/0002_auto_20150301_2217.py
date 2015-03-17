# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttemp',
            name='temp_val',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
