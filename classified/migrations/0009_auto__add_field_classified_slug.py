# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Classified.slug'
        db.add_column(u'classified_classified', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Classified.slug'
        db.delete_column(u'classified_classified', 'slug')


    models = {
        u'classified.classified': {
            'Meta': {'object_name': 'Classified'},
            u'classified_comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'classified_keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'classified_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['classified']