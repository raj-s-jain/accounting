# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20150413_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='time_spent',
        ),
    ]
