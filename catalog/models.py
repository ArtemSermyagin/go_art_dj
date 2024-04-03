from django.db import models
from django.urls import reverse

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.id}-{self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение"
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец'
    )

    def __str__(self):
        return f"{self.id}-{self.name}"

    def get_absolute_url(self):
        return reverse('detail_product', args=(self.pk,))

    class Meta:
        db_table = "products"
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    number = models.PositiveIntegerField(default=0, verbose_name="Номер")
    is_actual = models.BooleanField(default=False, verbose_name="Актуальная")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='versions',
        verbose_name="Продукт"
    )

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = "versions"
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
