# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'localchapters_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sections', to=orm['localchapters.LocalChaptersPage'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('heading_bar_color', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('textfield', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'localchapters', ['Section'])

        # Deleting field 'LocalChaptersPage.catalystpage_ptr'
        db.delete_column(u'localchapters_localchapterspage', u'catalystpage_ptr_id')

        # Adding field 'LocalChaptersPage.page_ptr'
        db.add_column(u'localchapters_localchapterspage', u'page_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['pages.Page'], unique=True, primary_key=True),
                      keep_default=False)

        # Adding field 'LocalChaptersPage.content'
        db.add_column(u'localchapters_localchapterspage', 'content',
                      self.gf('mezzanine.core.fields.RichTextField')(default=''),
                      keep_default=False)

        # Adding M2M table for field chapters on 'LocalChaptersPage'
        m2m_table_name = db.shorten_name(u'localchapters_localchapterspage_chapters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('localchapterspage', models.ForeignKey(orm[u'localchapters.localchapterspage'], null=False)),
            ('localchapter', models.ForeignKey(orm[u'localchapters.localchapter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['localchapterspage_id', 'localchapter_id'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'localchapters_section')


        # User chose to not deal with backwards NULL issues for 'LocalChaptersPage.catalystpage_ptr'
        raise RuntimeError("Cannot reverse this migration. 'LocalChaptersPage.catalystpage_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'LocalChaptersPage.catalystpage_ptr'
        db.add_column(u'localchapters_localchapterspage', u'catalystpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['custom.CatalystPage'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'LocalChaptersPage.page_ptr'
        db.delete_column(u'localchapters_localchapterspage', u'page_ptr_id')

        # Deleting field 'LocalChaptersPage.content'
        db.delete_column(u'localchapters_localchapterspage', 'content')

        # Removing M2M table for field chapters on 'LocalChaptersPage'
        db.delete_table(db.shorten_name(u'localchapters_localchapterspage_chapters'))


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
        },
        u'localchapters.localchapterspage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'LocalChaptersPage', '_ormbases': [u'pages.Page']},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'chapters'", 'blank': 'True', 'to': u"orm['localchapters.LocalChapter']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'localchapters.section': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Section'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'heading_bar_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['localchapters.LocalChaptersPage']"}),
            'textfield': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'font_awesome_icon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'navbar_title': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'title_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['localchapters']