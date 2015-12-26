# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='main_image',
            field=models.ImageField(null=True, upload_to=b'lessons/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='unit',
            name='main_image',
            field=models.ImageField(null=True, upload_to=b'units/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'courses/%Y/%m/%d'),
        ),
    ]
