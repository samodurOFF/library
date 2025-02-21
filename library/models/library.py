from django.db import models
from library.models import Book


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    library_url = models.URLField(max_length=100, blank=True, null=True)

    books = models.ManyToManyField(Book, related_name='libraries', through='Collection', blank=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    received_date = models.DateField(auto_now_add=True)


