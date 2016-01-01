# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0023_auto_20150705_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='archive',
            field=models.FileField(upload_to='', blank=True),
        ),
    ]
