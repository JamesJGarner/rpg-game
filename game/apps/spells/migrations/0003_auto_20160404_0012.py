# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0002_spell_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='name',
            field=models.CharField(max_length=140, unique=True),
        ),
    ]
