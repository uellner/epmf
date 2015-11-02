# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=155)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('summary', models.TextField(max_length=500)),
                ('description', models.TextField(verbose_name=b'course description')),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=155)),
                ('main_type', models.CharField(max_length=155)),
                ('content', models.TextField(verbose_name=b'lesson content')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=155)),
                ('summary', models.TextField(max_length=500)),
                ('content', models.TextField(verbose_name=b'unit content')),
                ('course', models.ForeignKey(to='lms.Course')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(to='lms.Unit'),
        ),
    ]
