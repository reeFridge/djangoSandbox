# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20150615_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descr',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='vdqphnfwar'),
        ),
    ]
