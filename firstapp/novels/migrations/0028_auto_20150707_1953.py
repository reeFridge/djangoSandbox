# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0027_auto_20150707_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strip',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('num', models.PositiveIntegerField(null=True)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='number',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='strip',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='novels.Issue'),
        ),
    ]
