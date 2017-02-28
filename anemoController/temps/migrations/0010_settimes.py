# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temps', '0009_auto_20170212_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetTimes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_set_date', models.DateTimeField(verbose_name=b'date time set')),
                ('set_first_time', models.DateTimeField(verbose_name=b'morning on time')),
                ('set_second_time', models.DateTimeField(verbose_name=b'morning off time')),
                ('set_third_time', models.DateTimeField(verbose_name=b'afternoon on time')),
                ('set_fourth_time', models.DateTimeField(verbose_name=b'afternoon off time')),
            ],
            options={
                'ordering': ['-time_set_date'],
                'get_latest_by': 'time_set_date',
            },
            bases=(models.Model,),
        ),
    ]
