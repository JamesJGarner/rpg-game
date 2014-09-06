# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Enemy.top'
        db.add_column(u'enemies_enemy', 'top',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=16, null=True),
                      keep_default=False)

        # Adding field 'Enemy.left'
        db.add_column(u'enemies_enemy', 'left',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=16, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Enemy.top'
        db.delete_column(u'enemies_enemy', 'top')

        # Deleting field 'Enemy.left'
        db.delete_column(u'enemies_enemy', 'left')


    models = {
        u'enemies.enemy': {
            'Meta': {'object_name': 'Enemy'},
            'health': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'top': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'null': 'True'})
        }
    }

    complete_apps = ['enemies']