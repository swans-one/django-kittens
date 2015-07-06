# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200, unique=True)),
                ('thumbnail', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('votes_up', models.PositiveIntegerField(default=0)),
                ('votes_down', models.PositiveIntegerField(default=0)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
