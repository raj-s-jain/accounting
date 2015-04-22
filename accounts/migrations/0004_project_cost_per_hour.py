# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_project_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cost_per_hour',
            field=models.FloatField(default=0.0),
        ),
    ]
