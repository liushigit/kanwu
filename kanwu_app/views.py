# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Book
from django.core.urlresolvers import reverse_lazy

class BookCreateView(CreateView):
    model = Book
    success_url = reverse_lazy('book_list')
    

class BookListView(ListView):
    model = Book
