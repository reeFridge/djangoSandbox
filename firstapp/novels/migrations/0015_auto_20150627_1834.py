# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0014_auto_20150627_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='subs',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='Subscribers'),
        ),
    ]
