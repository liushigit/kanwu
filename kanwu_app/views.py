# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Book

class BookCreateView(CreateView):
    model = Book

class BookListView(ListView):
    model = Book
