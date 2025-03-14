from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from library.models import Library, Book, Collection
import random


class Command(BaseCommand):
    help = 'Заполнение таблицы Collection существующими библиотеками и книгами'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            nargs='?',
            default=10,
            help='Количество связей Library-Book',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        libraries = Library.objects.all()
        books = Book.objects.all()

        existing_relations = set(Collection.objects.values_list("library_id", "book_id"))

        for _ in range(count):
            library = random.choice(libraries)
            book = random.choice(books)
            days_ago = random.randint(0, 365)

            if (library.id, book.id) not in existing_relations:
                Collection.objects.create(library=library, book=book,
                                          received_date=datetime.now() - timedelta(days=days_ago))
                existing_relations.add((library.id, book.id))
