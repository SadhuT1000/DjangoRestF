# flake8: noqa



import json


from django.core.management import BaseCommand, call_command
from django.core.management.base import BaseCommand
from django.core.serializers.base import DeserializationError

from lerning.models import Course
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            call_command("loaddata", "payment.json", verbosity=2)
            self.stdout.write(
                self.style.SUCCESS("Данные по платежам успешно загружены.")
            )
        except DeserializationError as e:
            self.stderr.write(self.style.ERROR(f"Ошибка десериализации: {e}"))

