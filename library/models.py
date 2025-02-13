from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    profile = models.URLField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])


    def __str__(self):
        return self.firstname + " " + self.lastname

# Create your models here.
