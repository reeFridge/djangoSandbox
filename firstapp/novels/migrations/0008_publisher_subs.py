# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('novels', '0007_auto_20150624_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='subs',
            field=models.ManyToManyField(related_name='Subscribers', to=settings.AUTH_USER_MODEL),
        ),
    ]
