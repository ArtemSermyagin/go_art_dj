from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        new_group, created = Group.objects.get_or_create(name='Модератор')
        ct = ContentType.objects.get_for_model(Product)
        permission_publish, created = Permission.objects.get_or_create(
            codename='set_published',
            name='Can publish posts',
            content_type=ct
        )
        permission_change, created = Permission.objects.get_or_create(
            codename='catalog.change_product',
            name='Can change Продукт',
            content_type=ct
        )
        new_group.permissions.add(permission_publish)
        new_group.permissions.add(permission_change)
