# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0002_auto_20150623_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arc',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
        ),
    ]
