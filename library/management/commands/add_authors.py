from random import choice
from django.utils import lorem_ipsum
from django.core.management.base import BaseCommand
import datetime

from library.models import Author


class Command(BaseCommand):
    help = 'Create random authors'

    firstnames = ["Алексей", "Дмитрий", "Сергей", "Павел", "Владимир", "Иван", "Михаил", "Андрей", "Егор", "Виктор"]
    lastnames = ["Иванов", "Петров", "Сидоров", "Козлов", "Смирнов", "Васильев", "Морозов", "Федоров", "Новиков",
                 "Михайлов"]
    birth_dates = [
        "1980-05-14",
        "1992-08-21",
        "1975-12-03",
        "2001-07-10",
        "1988-03-27",
        "1995-09-05",
        "1983-06-30",
        "1999-11-15",
        "1979-04-02",
        "2005-01-08",
    ]

    rates = list(range(0, 11))  # Рейтинг от 0 до 10

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int, help='Amount of authors')

    def handle(self, *args, **options):
        authors_amount = options.get('quantity')
        authors = [
            Author(
                firstname=choice(self.firstnames),
                lastname=choice(self.lastnames),
                birth_date=choice(self.birth_dates),
                rate=choice(self.rates),
            )
            for _ in range(authors_amount)  # Количество случайных объектов
        ]

        Author.objects.bulk_create(authors)
