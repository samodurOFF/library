from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    profile = models.URLField(
        null=True, blank=True, verbose_name="Ссылка на профиль", unique=True
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Удален",
        help_text="True - пользователь удален. Он не будет отображаться на сайте",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rate = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.firstname + " " + self.lastname

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


    class Meta:
        unique_together = (("firstname", "lastname", "birth_date"),)
        db_table = 'authors'
