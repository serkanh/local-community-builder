# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Techevent.name'
        db.delete_column('techvents_techevent', 'name')


    def backwards(self, orm):
        # Adding field 'Techevent.name'
        db.add_column('techvents_techevent', 'name',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=100),
                      keep_default=False)


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'swingtime.event': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swingtime.EventType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'swingtime.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swingtime.note': {
            'Meta': {'object_name': 'Note'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'techvents.techevent': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Techevent', '_ormbases': ['swingtime.Event']},
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['swingtime.Event']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['techvents']