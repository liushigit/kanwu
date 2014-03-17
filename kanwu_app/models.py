# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):
    # should the name be unique? 
    name = models.CharField(max_length=50, unique=True)
    def __unicode__(self):
        return self.name

class Press(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
	
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Press)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.title

class ErrorReport(models.Model):
    page_number = models.IntegerField()
    description = models.TextField(max_length=1000)
    book = models.ForeignKey(Book)
    
    
