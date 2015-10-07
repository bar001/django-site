# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(default=0, max_digits=2, decimal_places=2)),
                ('brand', models.ForeignKey(to='common.Brand')),
            ],
        ),
    ]
