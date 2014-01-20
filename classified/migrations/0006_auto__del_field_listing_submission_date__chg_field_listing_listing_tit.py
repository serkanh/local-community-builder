# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Listing.submission_date'
        db.delete_column(u'classified_listing', 'submission_date')


        # Changing field 'Listing.listing_title'
        db.alter_column(u'classified_listing', 'listing_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding field 'Listing.submission_date'
        db.add_column(u'classified_listing', 'submission_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Listing.listing_title'
        db.alter_column(u'classified_listing', 'listing_title', self.gf('django.db.models.fields.CharField')(default='test', max_length=100))

    models = {
        u'classified.listing': {
            'Meta': {'object_name': 'Listing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']