# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Match.user'
        db.delete_column(u'match_match', 'user_id')

        # Adding field 'Match.character'
        db.add_column(u'match_match', 'character',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['characters.Character']),
                      keep_default=False)

        # Adding field 'Match.character_health'
        db.add_column(u'match_match', 'character_health',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=3, max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'Match.character_rip'
        db.add_column(u'match_match', 'character_rip',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Match.user'
        db.add_column(u'match_match', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['characters.Character']),
                      keep_default=False)

        # Deleting field 'Match.character'
        db.delete_column(u'match_match', 'character_id')

        # Deleting field 'Match.character_health'
        db.delete_column(u'match_match', 'character_health')

        # Deleting field 'Match.character_rip'
        db.delete_column(u'match_match', 'character_rip')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'characters.character': {
            'Meta': {'object_name': 'Character'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Type']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '16', 'blank': 'True'})
        },
        u'characters.type': {
            'Meta': {'object_name': 'Type'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'enemies.enemy': {
            'Meta': {'object_name': 'Enemy'},
            'health': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'match.match': {
            'Meta': {'object_name': 'Match'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Character']"}),
            'character_health': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'blank': 'True'}),
            'character_rip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enemy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enemies.Enemy']"}),
            'enemy_health': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'blank': 'True'}),
            'enemy_rip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['match']