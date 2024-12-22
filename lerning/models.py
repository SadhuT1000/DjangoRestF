from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название курса", unique=True)

    description = models.TextField(verbose_name="Описание курса")

    preview = models.ImageField(
        upload_to="previews/courses/", blank=True, null=True, verbose_name="Картинка"
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

        def __str__(self):
            return self.name


class Lesson(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название урока", unique=True)

    description = models.TextField(verbose_name="Описание урока")

    preview = models.ImageField(
        upload_to="previews/lessons/", blank=True, null=True, verbose_name="Картинка"
    )

    link_video = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео",
        blank=True,
        null=True,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

        def __str__(self):
            return self.name


class Subscription(models.Model):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Курс",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return f"{self.user.email} подписка на {self.course.name}"
