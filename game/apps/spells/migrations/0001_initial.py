# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
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
                ('for_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Class')),
            ],
        ),
        migrations.CreateModel(
            name='SpellAcquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
                ('spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spells.Spell')),
            ],
            options={
                'verbose_name': 'Acquired Spell',
                'verbose_name_plural': 'Acquired Spells',
            },
        ),
        migrations.AlterUniqueTogether(
            name='spellacquired',
            unique_together=set([('character', 'spell')]),
        ),
    ]