# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0006_auto_20150624_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='arc',
            field=models.ForeignKey(blank=True, null=True, to='novels.Arc', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
