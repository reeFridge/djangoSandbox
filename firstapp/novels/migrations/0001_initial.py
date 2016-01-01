# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arc',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('arc_title', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=1000)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('real_name', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=1000)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=1000)),
                ('date', models.DateField(verbose_name='Creation date')),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name='Publication date')),
                ('desc', models.TextField(max_length=1000)),
                ('slug', models.SlugField(max_length=255)),
                ('arc', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Arc')),
                ('characters', models.ManyToManyField(related_name='Chars', to='novels.Character')),
                ('groups', models.ManyToManyField(related_name='IssueGroups', to='novels.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pub_title', models.CharField(max_length=255)),
                ('found', models.DateField(verbose_name='Foundation date')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('website', models.URLField(verbose_name='Website')),
                ('abbrev', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=1000)),
                ('date', models.DateField(verbose_name='Publication date')),
                ('slug', models.SlugField(max_length=255)),
                ('arc', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Arc')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Publisher')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Publisher'),
        ),
        migrations.AddField(
            model_name='issue',
            name='tit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Title'),
        ),
        migrations.AddField(
            model_name='group',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Publisher'),
        ),
        migrations.AddField(
            model_name='character',
            name='firstIssue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Issue'),
        ),
        migrations.AddField(
            model_name='character',
            name='groups',
            field=models.ManyToManyField(related_name='Groups', to='novels.Group'),
        ),
        migrations.AddField(
            model_name='character',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Publisher'),
        ),
        migrations.AddField(
            model_name='arc',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='novels.Publisher'),
        ),
    ]
