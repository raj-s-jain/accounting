# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20150420_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 44, 36, 935088)),
        ),
        migrations.AlterField(
            model_name='timespent',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 44, 36, 935996)),
        ),
    ]
