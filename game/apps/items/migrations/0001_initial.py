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
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'icon')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'items')),
                ('worth', models.DecimalField(decimal_places=2, max_digits=100)),
                ('level_required', models.PositiveIntegerField()),
                ('damage', models.PositiveIntegerField(default=0, null=True)),
                ('healing', models.PositiveIntegerField(default=0, null=True)),
                ('armor', models.PositiveIntegerField(default=0, null=True)),
                ('for_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Class')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Group')),
            ],
        ),
        migrations.CreateModel(
            name='ItemAcquired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='itemacquired',
            name='equipped_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Position'),
        ),
        migrations.AddField(
            model_name='itemacquired',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='position',
            field=models.ManyToManyField(default=None, to='items.Position'),
        ),
        migrations.AlterUniqueTogether(
            name='itemacquired',
            unique_together=set([('item', 'equipped_to')]),
        ),
    ]
