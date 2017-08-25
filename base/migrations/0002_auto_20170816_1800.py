# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay_data',
            name='img',
            field=models.CharField(max_length=500, verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='para_data',
            name='img',
            field=models.CharField(max_length=500, verbose_name='img'),
        ),
    ]
