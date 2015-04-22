# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_project_time_spent'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='time_spent',
            field=models.FloatField(default=0.0),
        ),
    ]
