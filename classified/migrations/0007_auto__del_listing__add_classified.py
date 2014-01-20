# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Listing'
        db.delete_table(u'classified_listing')

        # Adding model 'Classified'
        db.create_table(u'classified_classified', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'classified', ['Classified'])


    def backwards(self, orm):
        # Adding model 'Listing'
        db.create_table(u'classified_listing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'classified', ['Listing'])

        # Deleting model 'Classified'
        db.delete_table(u'classified_classified')


    models = {
        u'classified.classified': {
            'Meta': {'object_name': 'Classified'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']