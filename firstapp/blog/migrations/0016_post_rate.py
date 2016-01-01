# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
