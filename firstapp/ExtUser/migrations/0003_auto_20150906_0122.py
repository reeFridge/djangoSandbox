# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ExtUser', '0002_auto_20150906_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(verbose_name='uprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
