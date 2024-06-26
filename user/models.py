from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Почта", unique=True)
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар"
    )
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    country = models.CharField(max_length=255, verbose_name='Страна')
    verification_token = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Токен верификации"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
