# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Classified.listing_title'
        db.delete_column(u'classified_classified', 'listing_title')

        # Adding field 'Classified.classified_comments_count'
        db.add_column(u'classified_classified', u'classified_comments_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Classified.classified_keywords_string'
        db.add_column(u'classified_classified', u'classified_keywords_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Classified.classified_title'
        db.add_column(u'classified_classified', 'classified_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Classified.submission_date'
        db.add_column(u'classified_classified', 'submission_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Classified.listing_title'
        db.add_column(u'classified_classified', 'listing_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Classified.classified_comments_count'
        db.delete_column(u'classified_classified', u'classified_comments_count')

        # Deleting field 'Classified.classified_keywords_string'
        db.delete_column(u'classified_classified', u'classified_keywords_string')

        # Deleting field 'Classified.classified_title'
        db.delete_column(u'classified_classified', 'classified_title')

        # Deleting field 'Classified.submission_date'
        db.delete_column(u'classified_classified', 'submission_date')


    models = {
        u'classified.classified': {
            'Meta': {'object_name': 'Classified'},
            u'classified_comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'classified_keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'classified_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']