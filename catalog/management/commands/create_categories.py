import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    JSON_NAME = "db.json"

    @classmethod
    def path(cls):
        return f"{BASE_DIR}/fixtures/{cls.JSON_NAME}"

    @classmethod
    def json_read_categories(cls):
        with open(cls.path(), encoding="utf-8") as file:
            return [item for item in json.load(file) if item["model"] == "catalog.category"]

    @classmethod
    def json_read_products(cls):
        with open(cls.path(), encoding="utf-8") as file:
            return [item for item in json.load(file) if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category['fields'])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            category_id = product['fields'].pop('category')
            product_for_create.append(
                Product(
                    **product['fields'],
                    category=Category.objects.get(id=category_id)
                )
            )
        Product.objects.bulk_create(product_for_create)
