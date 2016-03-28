# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('level', models.PositiveIntegerField(default=1)),
                ('health', models.PositiveIntegerField(default=100)),
                ('top', models.PositiveIntegerField(null=True)),
                ('left', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]