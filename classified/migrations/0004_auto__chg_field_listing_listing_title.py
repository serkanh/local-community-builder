# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Listing.listing_title'
        db.alter_column(u'classified_listing', 'listing_title', self.gf('django.db.models.fields.CharField')(default='test', max_length=100))

    def backwards(self, orm):

        # Changing field 'Listing.listing_title'
        db.alter_column(u'classified_listing', 'listing_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    models = {
        u'classified.listing': {
            'Meta': {'object_name': 'Listing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'listing_comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'listing_keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'listing_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']