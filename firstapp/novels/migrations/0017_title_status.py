# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0016_auto_20150702_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='status',
            field=models.CharField(choices=[(0, 'Завершен'), (1, 'Незавершен')], default=(0, 'Завершен'), max_length=255),
        ),
    ]
