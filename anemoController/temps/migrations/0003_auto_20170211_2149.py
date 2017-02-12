# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0002_auto_20150321_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='recordedtemp',
            options={'get_latest_by': 'recorded_date'},
        ),
    ]
