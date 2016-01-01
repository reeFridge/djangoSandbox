# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]
