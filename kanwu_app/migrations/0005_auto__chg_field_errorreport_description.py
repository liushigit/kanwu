# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ErrorReport.description'
        db.alter_column(u'kanwu_app_errorreport', 'description', self.gf('django.db.models.fields.TextField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'ErrorReport.description'
        db.alter_column(u'kanwu_app_errorreport', 'description', self.gf('django.db.models.fields.CharField')(max_length=300))

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
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['kanwu_app.Book']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
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