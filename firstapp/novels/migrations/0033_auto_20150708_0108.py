# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0032_strip_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strip',
            name='num',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='strip',
            name='slug',
            field=models.SlugField(primary_key=True, blank=True, max_length=255, serialize=False),
        ),
    ]
