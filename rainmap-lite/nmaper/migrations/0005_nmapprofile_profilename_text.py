# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmaper', '0004_nmapscan_status_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='nmapprofile',
            name='profilename_text',
            field=models.CharField(default='Default', max_length=32),
            preserve_default=False,
        ),
    ]