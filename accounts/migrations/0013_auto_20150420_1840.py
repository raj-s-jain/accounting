# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20150420_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='project',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 4, 20)),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
