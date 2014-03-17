from django.conf.urls import patterns, include, url
from views import BookCreateView, BookListView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kanwu.views.home', name='home'),
    url(r'^books/create/', BookCreateView.as_view(), name="book_create"),
    url(r'^books/$', BookListView.as_view(), name="book_list"),
    # url(r'^kanwu/', include('kanwu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
