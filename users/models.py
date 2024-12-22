from django.contrib.auth.models import AbstractUser
from django.db import models

from lerning.models import Course, Lesson


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
    tg_nick = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Телега ник",
        help_text="Укажи телегу",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return self.email


class Payments(models.Model):
    CASH = "Наличные"
    TRANSFER = "Перевод на счет"

    STATUS_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    data = models.DateField(verbose_name="Дата платежа")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    payment_method = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default=TRANSFER,
        verbose_name="Метод оплаты",
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
