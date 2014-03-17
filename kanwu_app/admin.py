from django.contrib import admin
from models import Author, Press, Category, ErrorReport, Book

admin.site.register(Author)
admin.site.register(Press)
admin.site.register(Category)
admin.site.register(ErrorReport)
admin.site.register(Book)