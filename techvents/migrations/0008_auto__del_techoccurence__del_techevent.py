# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TechOccurence'
        db.delete_table('techvents_techoccurence')

        # Deleting model 'Techevent'
        db.delete_table('techvents_techevent')


    def backwards(self, orm):
        # Adding model 'TechOccurence'
        db.create_table('techvents_techoccurence', (
            ('techevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['techvents.Techevent'])),
            ('occurrence_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['swingtime.Occurrence'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('techvents', ['TechOccurence'])

        # Adding model 'Techevent'
        db.create_table('techvents_techevent', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['swingtime.Event'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('techvents', ['Techevent'])


    models = {
        
    }

    complete_apps = ['techvents']