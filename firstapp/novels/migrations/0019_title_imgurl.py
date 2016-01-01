# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0018_auto_20150702_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='imgUrl',
            field=models.URLField(verbose_name='Image', default='http://placehold.it/155x235'),
        ),
    ]
