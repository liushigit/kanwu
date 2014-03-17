# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Error'
        db.delete_table(u'kanwu_app_error')

        # Adding model 'ErrorReport'
        db.create_table(u'kanwu_app_errorreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_number', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'kanwu_app', ['ErrorReport'])


    def backwards(self, orm):
        # Adding model 'Error'
        db.create_table(u'kanwu_app_error', (
            ('page_number', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'kanwu_app', ['Error'])

        # Deleting model 'ErrorReport'
        db.delete_table(u'kanwu_app_errorreport')


    models = {
        u'kanwu_app.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'kanwu_app.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['kanwu_app.Author']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kanwu_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kanwu_app.Press']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'kanwu_app.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'kanwu_app.errorreport': {
            'Meta': {'object_name': 'ErrorReport'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'kanwu_app.press': {
            'Meta': {'object_name': 'Press'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['kanwu_app']