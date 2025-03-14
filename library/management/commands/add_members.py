from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Member, Library
from datetime import date

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет таблицу членов библиотеки случайными данными'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            default=10,
            help='Количество создаваемых членов',
        )

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for _ in range(count):
            member = Member(
                name=fake.first_name(),
                surname=fake.last_name(),
                email=fake.email(),
                gender=fake.random_element(Member.CHOICES_GENDER)[0],
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=90),
                role=fake.random_element(Member.CHOICES_ROLE)[0],
                is_active=fake.boolean(),
            )
            member.save()
