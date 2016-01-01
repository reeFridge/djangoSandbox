# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0024_issue_archive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='orig_title',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='title',
        ),
        migrations.AddField(
            model_name='issue',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
