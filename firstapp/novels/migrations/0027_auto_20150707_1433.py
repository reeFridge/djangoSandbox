# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0026_auto_20150707_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='characters',
            field=models.ManyToManyField(related_name='Chars', to='novels.Character', blank=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='groups',
            field=models.ManyToManyField(related_name='IssueGroups', to='novels.Group', blank=True),
        ),
    ]
