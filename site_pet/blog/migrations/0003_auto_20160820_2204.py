# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160820_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='text_content',
            field=models.TextField(),
        ),
    ]
