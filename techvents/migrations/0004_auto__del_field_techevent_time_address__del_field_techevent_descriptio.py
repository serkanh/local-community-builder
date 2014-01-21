# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Techevent.time_address'
        db.delete_column('techvents_techevent', 'time_address')

        # Deleting field 'Techevent.description'
        db.delete_column('techvents_techevent', 'description')

        # Deleting field 'Techevent.image'
        db.delete_column('techvents_techevent', 'image')

        # Deleting field 'Techevent.created_on'
        db.delete_column('techvents_techevent', 'created_on')

        # Deleting field 'Techevent.contact_email'
        db.delete_column('techvents_techevent', 'contact_email')

        # Deleting field 'Techevent.id'
        db.delete_column('techvents_techevent', 'id')

        # Deleting field 'Techevent.location_string'
        db.delete_column('techvents_techevent', 'location_string')

        # Deleting field 'Techevent.url'
        db.delete_column('techvents_techevent', 'url')

        # Deleting field 'Techevent.slug'
        db.delete_column('techvents_techevent', 'slug')

        # Deleting field 'Techevent.list_online'
        db.delete_column('techvents_techevent', 'list_online')

        # Deleting field 'Techevent.updated_on'
        db.delete_column('techvents_techevent', 'updated_on')

        # Adding field 'Techevent.event_ptr'
        db.add_column('techvents_techevent', 'event_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['swingtime.Event'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Techevent.time_address'
        db.add_column('techvents_techevent', 'time_address',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.description'
        db.add_column('techvents_techevent', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.image'
        db.add_column('techvents_techevent', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.created_on'
        db.add_column('techvents_techevent', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 20, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.contact_email'
        db.add_column('techvents_techevent', 'contact_email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.id'
        db.add_column('techvents_techevent', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'Techevent.location_string'
        db.add_column('techvents_techevent', 'location_string',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.url'
        db.add_column('techvents_techevent', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.slug'
        db.add_column('techvents_techevent', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.list_online'
        db.add_column('techvents_techevent', 'list_online',
                      self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Techevent.updated_on'
        db.add_column('techvents_techevent', 'updated_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 1, 20, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Deleting field 'Techevent.event_ptr'
        db.delete_column('techvents_techevent', 'event_ptr_id')


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
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['swingtime.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['techvents']