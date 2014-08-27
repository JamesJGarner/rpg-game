# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Spell.level_required'
        db.add_column(u'match_spell', 'level_required',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=15, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Spell.level_required'
        db.delete_column(u'match_spell', 'level_required')


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
            'health': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '16'}),
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
        u'match.attack': {
            'Meta': {'object_name': 'Attack'},
            'enemy_return_spell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reliation'", 'to': u"orm['match.Spell']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['match.Match']"}),
            'spell': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['match.Spell']"}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True'})
        },
        u'match.match': {
            'Meta': {'object_name': 'Match'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Character']"}),
            'character_health': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'blank': 'True'}),
            'enemy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['enemies.Enemy']"}),
            'enemy_health': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '16', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'match.spell': {
            'Meta': {'object_name': 'Spell'},
            'damage': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_required': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '15', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['match']