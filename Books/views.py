from django.views import generic

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
