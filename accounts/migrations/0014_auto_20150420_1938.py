# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20150420_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatedTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 19, 38, 45, 457794))),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 19, 38, 45, 456942)),
        ),
        migrations.AddField(
            model_name='updatedtime',
            name='project',
            field=models.ForeignKey(to='accounts.Project', null=True),
        ),
    ]
