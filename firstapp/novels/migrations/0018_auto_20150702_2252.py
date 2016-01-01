# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0017_title_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='artist',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='title',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
