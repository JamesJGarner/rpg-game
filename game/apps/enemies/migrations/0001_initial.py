# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Enemy'
        db.create_table(u'enemies_enemy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, max_length=16)),
            ('health', self.gf('django.db.models.fields.PositiveIntegerField')(default=100, max_length=16)),
        ))
        db.send_create_signal(u'enemies', ['Enemy'])


    def backwards(self, orm):
        # Deleting model 'Enemy'
        db.delete_table(u'enemies_enemy')


    models = {
        u'enemies.enemy': {
            'Meta': {'object_name': 'Enemy'},
            'health': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['enemies']