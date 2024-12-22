import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LinksValidator:
    def __init__(self, allowed_domains=None, field=None):
        if allowed_domains is None:
            allowed_domains = ["youtube.com"]
        self.allowed_domains = allowed_domains
        self.field = field  # Добавлен аргумент field

    def __call__(self, value):
        url_pattern = r"(https?://[^\\s]+)"
        urls = re.findall(url_pattern, value)

        for url in urls:
            if not any(domain in url for domain in self.allowed_domains):
                raise ValidationError(
                    _(
                        "Ссылка на сторонний ресурс обнаружена в поле %(field)s: %(url)s"
                    ),
                    params={
                        "field": self.field,
                        "url": url,
                    },  # Используем field для вывода в ошибке
                )


# from django.core.exceptions import ValidationError


# def validate_links(value):
#     youtube_pattern = r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.*$'
#
#     if not re.match(youtube_pattern, value):
#         raise ValidationError('ТУт можно только на Ютубб')

# from rest_framework.serializers import ValidationError
#
#
# class LinksValidator:
#     def __init__(self, field): # field - данные с которыми будут сравниваться входящие данные от пользователя
#         self.field = field
#
#     def __call__(self, value):  # value - те данные которые приходят от пользователя
#         link = dict(value).get(self.field)
#         # если в передаваемых данных value есть значение 'youtube.com' с ключом 'link', то:
#         if bool(dict(value).get('link')) and not bool('youtube.com' in link):
#             raise ValidationError('Недопустимая ссылка')
#
# # class LinksValidator:
# #
# #
# #
# def __init__(self, field):
#     self.field = field
#
# def __call__(self, value):
#     if isinstance(value, list):  # Если это список
#         for item in value:
#             if not isinstance(item, dict):  # Каждый элемент должен быть словарем
#                 raise ValidationError("Each item in the list must be a dictionary.")
#             tmp_val = item.get(self.field)
#             if not tmp_val:  # Проверяем, что поле существует и не пустое
#                 raise ValidationError(f"Field '{self.field}' is missing or empty in one of the items.")
#             print(f"Validated field: {tmp_val}")
#     elif isinstance(value, dict):  # Если это словарь
#         tmp_val = value.get(self.field)
#         if not tmp_val:  # Проверяем, что поле существует и не пустое
#             raise ValidationError(f"Field '{self.field}' is missing or empty.")
#         print(f"Validated field: {tmp_val}")
#     else:
#         raise ValidationError(f"Unsupported value type: {type(value)}")
#
