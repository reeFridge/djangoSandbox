# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0036_auto_20150708_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='thumbnail',
        ),
    ]
