# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_publisher_imgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='pub_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 24, 8, 51, 31, 844399, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
