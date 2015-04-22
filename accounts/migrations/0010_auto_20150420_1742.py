# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20150420_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 42, 6, 511792)),
        ),
        migrations.AlterField(
            model_name='timespent',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 42, 6, 512594)),
        ),
    ]
