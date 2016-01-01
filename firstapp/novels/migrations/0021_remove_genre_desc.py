# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0020_auto_20150703_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='desc',
        ),
    ]
