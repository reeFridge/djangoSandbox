# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0011_auto_20150627_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='imprint_of',
        ),
        migrations.AddField(
            model_name='publisher',
            name='imprint_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True, to='novels.Publisher'),
        ),
    ]
