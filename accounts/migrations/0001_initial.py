# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=90)),
                ('company_info', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=90)),
                ('tech_used', models.CharField(max_length=90)),
                ('time_spent', models.TimeField()),
                ('start_date', models.DateField(default=datetime.date(2015, 4, 7))),
                ('client', models.ForeignKey(to='accounts.Client')),
            ],
        ),
    ]
