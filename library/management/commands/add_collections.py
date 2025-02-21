from django.core.management.base import BaseCommand
import random
from library.models import Library, Book, Collection
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Заполняет таблицу Collection случайными данными'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=50,
            help='Количество записей, которые нужно создать в таблице Collection',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        libraries = Library.objects.all()
        books = Book.objects.all()

        for _ in range(count):
            library = random.choice(libraries)
            book = random.choice(books)


            start_date = date(2000, 1, 1)
            end_date = date.today()
            random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


            collection = Collection(
                library=library,
                book=book,
                received_date=random_date
            )
            collection.save()
