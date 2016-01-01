# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0022_title_translateurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='status',
            field=models.CharField(default=('Завершен', 'Completed'), max_length=255, choices=[('Завершен', 'Completed'), ('Незавершен', 'Ongoing')]),
        ),
    ]
