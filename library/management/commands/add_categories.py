from random import choice
from django.core.management.base import BaseCommand
from library.models import Author, Category


class Command(BaseCommand):
    help = 'Create categories'

    book_categories = [
        "Художественная литература",
        "Научная литература",
        "Учебная литература",
        "Бизнес-литература",
        "Техническая литература",
        "Медицинская литература",
        "Философия и религия",
        "Психология и саморазвитие",
        "История",
        "Биографии и мемуары",
        "Документальная литература",
        "Публицистика",
        "Кулинария",
        "Дом, сад и быт",
        "Путеводители и путешествия",
        "Искусство и культура",
        "Музыка и кино",
        "Компьютеры и IT",
        "Детская литература",
        "Подростковая литература",
        "Энциклопедии и справочники",
        "Спорт и здоровье",
        "Военная литература",
        "Право и законодательство",
        "Экономика и финансы",
        "Политика и общество",
        "Эзотерика и астрология",
    ]

    def handle(self, *args, **options):
        categories = [
            Category(
                name=category
            )
            for category in self.book_categories  # Количество случайных объектов
        ]

        Category.objects.bulk_create(categories)
