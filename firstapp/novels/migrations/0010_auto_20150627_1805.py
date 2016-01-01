# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0009_publisher_imprints'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='imprints',
        ),
        migrations.AddField(
            model_name='publisher',
            name='is_imprint',
            field=models.ManyToManyField(related_name='Imprint_of', to='novels.Publisher'),
        ),
    ]
