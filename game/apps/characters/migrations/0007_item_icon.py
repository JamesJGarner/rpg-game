# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20160323_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=b'icon'),
        ),
    ]
