# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20150420_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 56, 4, 857742))),
            ],
        ),
        migrations.RemoveField(
            model_name='timespent',
            name='project',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 56, 4, 856815)),
        ),
        migrations.DeleteModel(
            name='TimeSpent',
        ),
        migrations.AddField(
            model_name='time',
            name='project',
            field=models.ForeignKey(to='accounts.Project', null=True),
        ),
    ]
