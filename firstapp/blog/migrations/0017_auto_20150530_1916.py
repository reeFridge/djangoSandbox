# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imgURL',
            field=models.CharField(default='http://placehold.it/200x140', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
