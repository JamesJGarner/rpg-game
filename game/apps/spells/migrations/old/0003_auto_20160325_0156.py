 -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 01:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_auto_20160325_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='type',
            new_name='for_class',
        ),
    ]