# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalChapter'
        db.create_table(u'localchapters_localchapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('schoolName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('schoolAddress', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('chapterWebsite', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('chapterNumber', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('chapterEmail', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'localchapters', ['LocalChapter'])


    def backwards(self, orm):
        # Deleting model 'LocalChapter'
        db.delete_table(u'localchapters_localchapter')


    models = {
        u'localchapters.localchapter': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'LocalChapter'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'chapterEmail': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'chapterNumber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'chapterWebsite': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schoolAddress': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolName': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['localchapters']