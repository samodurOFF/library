from django.db import models
from library.models import Book


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    library_url = models.URLField(max_length=100, blank=True, null=True)

    books = models.ManyToManyField(Book, related_name='libraries', blank=True, null=True)

    def __str__(self):
        return self.name

