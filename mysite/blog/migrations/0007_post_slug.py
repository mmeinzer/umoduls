# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True),
        ),
    ]
