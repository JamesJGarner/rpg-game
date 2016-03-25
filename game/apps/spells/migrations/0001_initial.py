# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0007_item_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField(null=True)),
                ('damage', models.PositiveIntegerField()),
                ('level_required', models.PositiveIntegerField(null=True)),
                ('turn_cooldown', models.PositiveIntegerField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Type')),
            ],
        ),
    ]