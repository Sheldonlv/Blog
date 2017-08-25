# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Num', models.CharField(max_length=20, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('viewed', models.CharField(max_length=20, verbose_name='\u9605\u8bfb\u6b21\u6570')),
            ],
        ),
        migrations.CreateModel(
            name='essay_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Num', models.CharField(max_length=20, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='img')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('up_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='para_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Num', models.CharField(max_length=20, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('img', models.CharField(max_length=200, verbose_name='img')),
                ('writer', models.CharField(max_length=30, verbose_name='\u4f5c\u8005')),
                ('doc_type', models.CharField(max_length=20, verbose_name='\u7c7b\u578b')),
                ('reco', models.CharField(max_length=5, verbose_name='\u63a8\u8350')),
                ('content', models.TextField(verbose_name='\u6458\u8981')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('up_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
        ),
    ]
