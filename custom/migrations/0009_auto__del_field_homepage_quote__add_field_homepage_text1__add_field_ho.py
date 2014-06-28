# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HomePage.quote'
        db.delete_column(u'custom_homepage', 'quote')

        # Adding field 'HomePage.text1'
        db.add_column(u'custom_homepage', 'text1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.quoteA'
        db.add_column(u'custom_homepage', 'quoteA',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section2Title'
        db.add_column(u'custom_homepage', 'section2Title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section2SubTitle'
        db.add_column(u'custom_homepage', 'section2SubTitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section2Color'
        db.add_column(u'custom_homepage', 'section2Color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section2ButtonTitle'
        db.add_column(u'custom_homepage', 'section2ButtonTitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section3BackgroundPicture'
        db.add_column(u'custom_homepage', 'section3BackgroundPicture',
                      self.gf('mezzanine.core.fields.FileField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'HomePage.section3ButtonTitle'
        db.add_column(u'custom_homepage', 'section3ButtonTitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section3Link'
        db.add_column(u'custom_homepage', 'section3Link',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section4Title'
        db.add_column(u'custom_homepage', 'section4Title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'HomePage.section4BackgroundColor'
        db.add_column(u'custom_homepage', 'section4BackgroundColor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding M2M table for field blog_posts on 'HomePage'
        m2m_table_name = db.shorten_name(u'custom_homepage_blog_posts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('homepage', models.ForeignKey(orm[u'custom.homepage'], null=False)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['homepage_id', 'blogpost_id'])


    def backwards(self, orm):
        # Adding field 'HomePage.quote'
        db.add_column(u'custom_homepage', 'quote',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'HomePage.text1'
        db.delete_column(u'custom_homepage', 'text1')

        # Deleting field 'HomePage.quoteA'
        db.delete_column(u'custom_homepage', 'quoteA')

        # Deleting field 'HomePage.section2Title'
        db.delete_column(u'custom_homepage', 'section2Title')

        # Deleting field 'HomePage.section2SubTitle'
        db.delete_column(u'custom_homepage', 'section2SubTitle')

        # Deleting field 'HomePage.section2Color'
        db.delete_column(u'custom_homepage', 'section2Color')

        # Deleting field 'HomePage.section2ButtonTitle'
        db.delete_column(u'custom_homepage', 'section2ButtonTitle')

        # Deleting field 'HomePage.section3BackgroundPicture'
        db.delete_column(u'custom_homepage', 'section3BackgroundPicture')

        # Deleting field 'HomePage.section3ButtonTitle'
        db.delete_column(u'custom_homepage', 'section3ButtonTitle')

        # Deleting field 'HomePage.section3Link'
        db.delete_column(u'custom_homepage', 'section3Link')

        # Deleting field 'HomePage.section4Title'
        db.delete_column(u'custom_homepage', 'section4Title')

        # Deleting field 'HomePage.section4BackgroundColor'
        db.delete_column(u'custom_homepage', 'section4BackgroundColor')

        # Removing M2M table for field blog_posts on 'HomePage'
        db.delete_table(db.shorten_name(u'custom_homepage_blog_posts'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blog.blogcategory': {
            'Meta': {'ordering': "(u'title',)", 'object_name': 'BlogCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'blog.blogpost': {
            'Meta': {'ordering': "(u'-publish_date',)", 'object_name': 'BlogPost'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'blogposts'", 'blank': 'True', 'to': u"orm['blog.BlogCategory']"}),
            u'comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'rating_average': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'rating_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'rating_sum': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_posts_rel_+'", 'blank': 'True', 'to': u"orm['blog.BlogPost']"}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'blogposts'", 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'custom.catalystpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'CatalystPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'custom.gridpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'GridPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'custom.gridsection': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'GridSection'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gridsection'", 'to': u"orm['custom.GridPage']"}),
            'textfield': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'custom.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'blog_posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'pressreleases'", 'blank': 'True', 'to': u"orm['blog.BlogPost']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'quoteA': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quoteAttr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'quoteColor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section2ButtonTitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section2Color': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section2SubTitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section2Title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section3BackgroundPicture': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            'section3ButtonTitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section3Link': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section4BackgroundColor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'section4Title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'custom.section': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Section'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'heading_bar_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['custom.CatalystPage']"}),
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

    complete_apps = ['custom']