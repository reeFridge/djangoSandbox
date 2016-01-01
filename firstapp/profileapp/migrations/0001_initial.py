# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import profileapp.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', profileapp.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile', primary_key=True, verbose_name='User', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('work', models.CharField(verbose_name='Работа', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='work',
            field=models.ForeignKey(verbose_name='Вид деятельности', to='profileapp.Work'),
        ),
    ]
