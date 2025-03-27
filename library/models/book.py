from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import ForeignKey

from library.models.category import Category


class Book(models.Model):
    CHOICES = (
        ("fiction", "Fiction"),
        ("non-fiction", "Non-Fiction"),
        ("science fiction", "Science Fiction"),
        ("fantasy", "Fantasy"),
        ("mystery", "Mystery"),
        ("biography", "Biography"),
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    author = models.ForeignKey("Author", verbose_name='Author', null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', null=True,
                                 related_name="books")
    publish_date = models.DateField()
    publish = models.ForeignKey("Member", on_delete=models.CASCADE, verbose_name='Publisher', null=True, db_column='publish')
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    pages = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(1000)]
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Owner', related_name='books', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'
