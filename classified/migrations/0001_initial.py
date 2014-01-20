# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Listing'
        db.create_table(u'classified_listing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'classified', ['Listing'])


    def backwards(self, orm):
        # Deleting model 'Listing'
        db.delete_table(u'classified_listing')


    models = {
        u'classified.listing': {
            'Meta': {'object_name': 'Listing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['classified']