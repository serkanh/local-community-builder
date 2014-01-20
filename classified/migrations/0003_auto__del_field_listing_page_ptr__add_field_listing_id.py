# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Listing.page_ptr'
        db.delete_column(u'classified_listing', u'page_ptr_id')

        # Adding field 'Listing.id'
        db.add_column(u'classified_listing', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Listing.page_ptr'
        db.add_column(u'classified_listing', u'page_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['pages.Page'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Listing.id'
        db.delete_column(u'classified_listing', u'id')


    models = {
        u'classified.listing': {
            'Meta': {'object_name': 'Listing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'listing_comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'listing_keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'listing_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']