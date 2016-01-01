# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0033_auto_20150708_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='issue',
            name='trans_name',
            field=models.CharField(blank=True, null=True, max_length=255),
        ),
    ]
