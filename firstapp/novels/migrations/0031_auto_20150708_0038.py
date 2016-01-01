# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0030_auto_20150708_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strip',
            name='id',
        ),
        migrations.AlterField(
            model_name='strip',
            name='num',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
