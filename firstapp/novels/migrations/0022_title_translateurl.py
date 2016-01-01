# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0021_remove_genre_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='translateURL',
            field=models.URLField(default='http://', verbose_name='Trans'),
        ),
    ]
