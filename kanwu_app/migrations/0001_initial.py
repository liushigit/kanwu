# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'kanwu_app_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'kanwu_app', ['Author'])

        # Adding model 'Press'
        db.create_table(u'kanwu_app_press', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'kanwu_app', ['Press'])

        # Adding model 'Category'
        db.create_table(u'kanwu_app_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'kanwu_app', ['Category'])

        # Adding model 'Error'
        db.create_table(u'kanwu_app_error', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_number', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'kanwu_app', ['Error'])

        # Adding model 'Book'
        db.create_table(u'kanwu_app_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kanwu_app.Press'])),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['kanwu_app.Category'])),
        ))
        db.send_create_signal(u'kanwu_app', ['Book'])

        # Adding M2M table for field author on 'Book'
        m2m_table_name = db.shorten_name(u'kanwu_app_book_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'kanwu_app.book'], null=False)),
            ('author', models.ForeignKey(orm[u'kanwu_app.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'kanwu_app_author')

        # Deleting model 'Press'
        db.delete_table(u'kanwu_app_press')

        # Deleting model 'Category'
        db.delete_table(u'kanwu_app_category')

        # Deleting model 'Error'
        db.delete_table(u'kanwu_app_error')

        # Deleting model 'Book'
        db.delete_table(u'kanwu_app_book')

        # Removing M2M table for field author on 'Book'
        db.delete_table(db.shorten_name(u'kanwu_app_book_author'))


    models = {
        u'kanwu_app.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'kanwu_app.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['kanwu_app.Author']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kanwu_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kanwu_app.Press']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'kanwu_app.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'kanwu_app.error': {
            'Meta': {'object_name': 'Error'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'kanwu_app.press': {
            'Meta': {'object_name': 'Press'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['kanwu_app']