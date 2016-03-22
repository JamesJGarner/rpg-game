# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20160322_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteritem',
            name='equipped_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Position'),
        ),
    ]
