# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0008_publisher_subs'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='imprints',
            field=models.ManyToManyField(to='novels.Publisher', related_name='Imprints'),
        ),
    ]
