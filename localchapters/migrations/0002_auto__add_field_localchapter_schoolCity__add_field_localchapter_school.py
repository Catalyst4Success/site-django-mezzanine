# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LocalChapter.schoolCity'
        db.add_column(u'localchapters_localchapter', 'schoolCity',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 6, 26, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'LocalChapter.schoolState'
        db.add_column(u'localchapters_localchapter', 'schoolState',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'LocalChapter.schoolZipCode'
        db.add_column(u'localchapters_localchapter', 'schoolZipCode',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LocalChapter.schoolCity'
        db.delete_column(u'localchapters_localchapter', 'schoolCity')

        # Deleting field 'LocalChapter.schoolState'
        db.delete_column(u'localchapters_localchapter', 'schoolState')

        # Deleting field 'LocalChapter.schoolZipCode'
        db.delete_column(u'localchapters_localchapter', 'schoolZipCode')


    models = {
        u'localchapters.localchapter': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'LocalChapter'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'chapterEmail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'chapterNumber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'chapterWebsite': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schoolAddress': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolCity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolState': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'schoolZipCode': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['localchapters']