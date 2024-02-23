from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    descriptions = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "categories"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    descriptions = models.TextField(verbose_name="Описание")
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

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "products"
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
