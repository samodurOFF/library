from django.core.management.base import BaseCommand
from library.models import Book, Author, Category, Member
from faker import Faker


fake = Faker()

class Command(BaseCommand):
    help = 'Заполняет таблицу книг случайными данными'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=50,
            help='Количество создаваемых книг',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        authors = Author.objects.all()
        categories = Category.objects.all()
        members = Member.objects.all()

        for _ in range(count):
            author = authors[fake.random_int(0, len(authors)-1)]
            category = categories[fake.random_int(0, len(categories)-1)]
            member = members[fake.random_int(0, len(members)-1)]

            book = Book(
                title=fake.sentence(nb_words=4),
                author_id=author,
                category_id=category,
                publish_date=fake.date_this_century(),
                publish_id=member,
                description=fake.text(),
                genre=fake.random_element(Book.CHOICES)[0],
                pages=fake.random_int(100, 1000),
            )
            book.save()
