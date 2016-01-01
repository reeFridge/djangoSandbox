# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0010_auto_20150627_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='is_imprint',
            new_name='imprint_of',
        ),
    ]
