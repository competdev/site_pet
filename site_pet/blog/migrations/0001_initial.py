# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 12:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.upload_helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('text_call', models.CharField(max_length=255, verbose_name='Descrição')),
                ('text_content', models.TextField(verbose_name='Conteúdo')),
                ('thumbnail', models.ImageField(upload_to=utils.upload_helper.get_image_path, verbose_name='Thumbnail')),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('last_modification', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='members.Member', verbose_name='Autor')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts (todos)',
            },
        ),
        migrations.CreateModel(
            name='MyPost',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': 'Post',
            },
            bases=('blog.post',),
        ),
    ]
