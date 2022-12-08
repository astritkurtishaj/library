from django.shortcuts import render, redirect, reverse, get_object_or_404

from authors.models import Author
from .models import Book
from .histogram import process_file, different_words, most_common_words, total_words
from django.views import generic
from .forms import BookForm


class HomeView(generic.ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    print('context_object_name', context_object_name)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

    def get_queryset(self):
        fields = {'book_name': 'book_name__icontains', 'book_genre': 'book_genre__icontains', 'author': 'author__id'}
        kwargs = {fields[name]: value for name, value in self.request.GET.items() if name in fields and value}
        return self.model.objects.filter(**kwargs) if kwargs else self.model.objects.all()


class CreateView(generic.CreateView):
    form_class = BookForm
    template_name = 'books/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context


# def create(request):
#     authors = Author.objects.all()
#     if request.method == 'GET':
#         return render(request, 'books/create.html', {'authors': authors})
#     elif request.method == 'POST':
#         book_name = request.POST['book_name']
#         book_genre = request.POST['book_genre']
#         book_file = request.FILES['book_file']
#
#         author_pk = request.POST['author']
#         author = Author.objects.get(pk=author_pk)
#         book = Book(book_name=book_name, book_genre=book_genre, author=author, book_file=book_file)
#         book.save()
#     return redirect(reverse('books:home'))


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        hist = process_file(book.book_file.path)
        print(hist)
        context['total_words'] = total_words(hist)
        context['most_common_words'] = most_common_words(hist, 10)
        context['different_words'] = different_words(hist)
        print('context', context)
        return context

# def detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     hist = process_file(book.book_file.path)
#     context = {
#         'book': book,
#         'total_words': total_words(hist),
#         'most_common_words': most_common_words(hist, 10),
#         'different_words': different_words(hist),
#     }
#
#     return render(request=request, template_name='books/detail.html', context=context)
