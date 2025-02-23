import json
import sys
from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Экспортирует данные из SQLite в JSON с указанной кодировкой.'

    def handle(self, *args, **options):
        data = []
        for model in apps.get_models():
            table_name = model._meta
            for record in model.objects.all().values():
                pk, *other = record.items()
                data.append(
                    {
                        "model": table_name,
                        "pk": pk[1],
                        "fields": dict(other)
                    },
                )
        with open('dump.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4, default=str))


