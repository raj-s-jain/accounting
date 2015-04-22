# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20150420_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSpent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 41, 22, 840416))),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 17, 41, 22, 839229)),
        ),
        migrations.AddField(
            model_name='timespent',
            name='project',
            field=models.ForeignKey(to='accounts.Project', null=True),
        ),
    ]
