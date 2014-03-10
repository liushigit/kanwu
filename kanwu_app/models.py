from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

class Press(models.Model):
    name = models.CharField(max_length=50)
	
class Category(models.Model):
    name = models.CharField(max_length=50)

class Error(models.Model):
    page_number = models.IntegerField()
    description = models.CharField(max_length=300)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Press)
    isbn = models.CharField(max_length=20)
    category = models.ForeignKey(Category)
