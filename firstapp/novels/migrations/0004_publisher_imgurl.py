# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0003_auto_20150623_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='imgUrl',
            field=models.URLField(default='http://placehold.it/150x150', verbose_name='Image'),
        ),
    ]
