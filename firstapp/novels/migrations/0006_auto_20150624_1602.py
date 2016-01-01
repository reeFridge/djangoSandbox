# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0005_issue_pub_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='arc',
            name='orig_arc_title',
            field=models.CharField(max_length=255, default='Original Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='orig_title',
            field=models.CharField(max_length=255, default='Original Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='orig_title',
            field=models.CharField(max_length=255, default='Original Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='orig_title',
            field=models.CharField(max_length=255, default='Original'),
            preserve_default=False,
        ),
    ]
