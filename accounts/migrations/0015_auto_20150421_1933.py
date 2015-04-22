# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20150420_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatedtime',
            name='time_spent',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 19, 33, 14, 765228)),
        ),
        migrations.AlterField(
            model_name='updatedtime',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 21, 19, 33, 14, 766074)),
        ),
    ]
