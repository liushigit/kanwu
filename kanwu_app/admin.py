from django.contrib import admin
from models import Author, Press, Category, ErrorReport, Book

class ErrorReportInline(admin.StackedInline):
    model = ErrorReport
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [ErrorReportInline, ]

admin.site.register(Author)
admin.site.register(Press)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)

