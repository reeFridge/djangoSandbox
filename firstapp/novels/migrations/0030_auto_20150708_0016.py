# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0029_remove_issue_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strip',
            name='img',
        ),
        migrations.AddField(
            model_name='strip',
            name='img_file_name',
            field=models.CharField(default='01.jpg', max_length=50),
            preserve_default=False,
        ),
    ]
