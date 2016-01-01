# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20150612_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rate',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='ambplvojdc'),
        ),
    ]
