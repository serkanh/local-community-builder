# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Listing.listing_comments_count'
        db.delete_column(u'classified_listing', u'listing_comments_count')

        # Deleting field 'Listing.listing_keywords_string'
        db.delete_column(u'classified_listing', u'listing_keywords_string')


    def backwards(self, orm):
        # Adding field 'Listing.listing_comments_count'
        db.add_column(u'classified_listing', u'listing_comments_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Listing.listing_keywords_string'
        db.add_column(u'classified_listing', u'listing_keywords_string',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    models = {
        u'classified.listing': {
            'Meta': {'object_name': 'Listing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']