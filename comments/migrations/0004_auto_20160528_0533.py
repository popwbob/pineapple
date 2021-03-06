# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20160514_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcomment',
            name='content',
            field=models.TextField(max_length=512, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(max_length=512, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='topiccomment',
            name='content',
            field=models.TextField(max_length=512, verbose_name='评论内容'),
        ),
    ]
