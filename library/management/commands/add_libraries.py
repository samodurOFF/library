from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Library, Member

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет таблицу библиотек случайными данными'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=10,
            help='Количество создаваемых библиотек',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            library = Library(
                name=fake.company(),
                location=fake.city(),
                library_url=fake.url(),
            )
            library.save()
