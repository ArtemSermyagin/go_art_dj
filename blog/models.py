from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, verbose_name='Слаг')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    number_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "blogs"
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
