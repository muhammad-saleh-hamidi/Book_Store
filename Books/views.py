from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/detail_book.html'


class BookCreatView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'book/book_creat.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'book/book_update.html'  # Usually the same as the creat page
    fields = ['title', 'author', 'description', 'price']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('book_list')
