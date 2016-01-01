# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0031_auto_20150708_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='strip',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
    ]
