from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):
    full_name = models.CharField(max_length=300)
    biography = models.TextField()

    def get_absolute_url(self):
        return reverse_lazy('authors:home')
