# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('title', models.CharField(max_length=250)),
                ('venue', models.CharField(max_length=250)),
                ('description', models.TextField(default=b' ')),
                ('volunteers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]
