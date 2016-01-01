# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0035_issue_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='thumbnail',
            field=models.ForeignKey(related_name='Thumbnail_Issue', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='novels.Strip'),
        ),
    ]
