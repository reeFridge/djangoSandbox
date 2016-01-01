# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_auto_20150606_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='likes'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='wgpicnyoqx'),
        ),
    ]
