from django.db import models
from datetime import date
from library.models import Library


class Member(models.Model):
    CHOICES_GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    CHOICES_ROLE = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('reader', 'Reader'),
    ]

    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email", unique=True)
    gender = models.CharField(choices=CHOICES_GENDER, verbose_name='Пол', max_length=50)
    birth_date = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(blank=False, null=False)
    role = models.CharField(choices=CHOICES_ROLE, verbose_name='Роль', max_length=50)
    is_active = models.BooleanField(default=True)
    libraries = models.ManyToManyField(Library, related_name='members')

    def save(self, *args, **kwargs):
        today = date.today()
        self.age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        unique_together = (('name', 'surname', 'birth_date'),)
        db_table = 'members'
