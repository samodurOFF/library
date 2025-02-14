from django.core.validators import MaxValueValidator
from django.db import models
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
    author_id = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Category ID' ,null=True, related_name="books")
    publish_date = models.DateField()
    publish_id = models.ForeignKey("Member", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    pages = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(1000)]
    )

    def __str__(self):
        return self.title
