# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Character_Items'
        db.delete_table(u'characters_character_items')

        # Adding model 'CharacterItem'
        db.create_table(u'characters_characteritem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Character'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Item'])),
            ('is_currently_equipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'characters', ['CharacterItem'])


    def backwards(self, orm):
        # Adding model 'Character_Items'
        db.create_table(u'characters_character_items', (
            ('is_currently_equipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Item'])),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Character'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'characters', ['Character_Items'])

        # Deleting model 'CharacterItem'
        db.delete_table(u'characters_characteritem')


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
            'Meta': {'ordering': "['name']", 'object_name': 'Character'},
            'health': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inv_bag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.InvBag']", 'null': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Type']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'xp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '16', 'blank': 'True'})
        },
        u'characters.characteritem': {
            'Meta': {'object_name': 'CharacterItem'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_currently_equipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Item']"})
        },
        u'characters.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'characters.invbag': {
            'Meta': {'object_name': 'InvBag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_required': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'spaces': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '100'}),
            'worth': ('django.db.models.fields.DecimalField', [], {'max_digits': '100', 'decimal_places': '2'})
        },
        u'characters.item': {
            'Meta': {'object_name': 'Item'},
            'armor': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '200', 'null': 'True'}),
            'damage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '200', 'null': 'True'}),
            'for_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Type']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Group']"}),
            'healing': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level_required': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'worth': ('django.db.models.fields.DecimalField', [], {'max_digits': '100', 'decimal_places': '2'})
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
        }
    }

    complete_apps = ['characters']