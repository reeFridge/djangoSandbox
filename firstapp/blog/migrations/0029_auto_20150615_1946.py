# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20150612_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='xwgpbonvmk'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
