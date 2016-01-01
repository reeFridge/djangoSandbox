# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0034_auto_20150708_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='thumbnail',
            field=models.ForeignKey(related_name='Thumbnail_Issue', on_delete=django.db.models.deletion.SET_NULL, to='novels.Strip', null=True),
        ),
    ]
