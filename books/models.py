from django.db import models
from authors.models import Author
from django.urls import reverse_lazy


class Book(models.Model):
    book_name = models.CharField(max_length=250)
    book_genre = models.CharField(max_length=100)
    book_file = models.FileField(upload_to='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse_lazy('books:home')
