from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="телофон",
        blank=True,
        null=True,
        help_text="введи номер телефона",
    )
    city = models.CharField(max_length=50, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="photo/avatars/", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return self.email
