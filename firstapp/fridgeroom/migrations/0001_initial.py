# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='Publication date')),
            ],
        ),
        migrations.CreateModel(
            name='StandartPublication',
            fields=[
                ('publication_ptr', models.OneToOneField(parent_link=True, serialize=False, to='fridgeroom.Publication', primary_key=True, auto_created=True)),
                ('content', models.TextField(max_length=1000)),
            ],
            bases=('fridgeroom.publication',),
        ),
    ]
