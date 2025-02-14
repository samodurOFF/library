from django.core.validators import MaxValueValidator
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Издательство")
    address = models.TextField(null=True, blank=True, verbose_name="Адрес")
    city = models.TextField(null=True, blank=True, max_length=100, verbose_name="Город")
    country = models.TextField(
        null=True, blank=True, max_length=100, verbose_name="Страна"
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Телефон"
    )

    def __str__(self):
        return self.name

