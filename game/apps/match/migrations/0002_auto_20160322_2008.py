# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='damage_dealt',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attack',
            name='damage_taken',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='character_health',
            field=models.PositiveIntegerField(blank=True, verbose_name=b'Current Character Health'),
        ),
        migrations.AlterField(
            model_name='match',
            name='enemy_health',
            field=models.PositiveIntegerField(blank=True, verbose_name=b'Current Enemy Health'),
        ),
        migrations.AlterField(
            model_name='match',
            name='resource',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='spell',
            name='damage',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='spell',
            name='level_required',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='turn_cooldown',
            field=models.PositiveIntegerField(),
        ),
    ]