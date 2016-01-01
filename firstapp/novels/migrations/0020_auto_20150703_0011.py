# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0019_title_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='status',
            field=models.CharField(max_length=255, default=('Complete', 'Завершен'), choices=[('Complete', 'Завершен'), ('Ongoing', 'Незавершен')]),
        ),
    ]
