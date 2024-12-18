from django.core.management.base import BaseCommand

from lerning.models import Course
from users.models import Payments, User
import json

from django.core.management import BaseCommand, call_command
from django.core.serializers.base import DeserializationError




class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            call_command('loaddata', 'payment.json', verbosity=2)
            self.stdout.write(self.style.SUCCESS('Данные по платежам успешно загружены.'))
        except DeserializationError as e:
            self.stderr.write(self.style.ERROR(f'Ошибка десериализации: {e}'))

        # user = User.objects.get(email="admin@mail.com")
        # paid_course = Course.objects.get(title="Data_engineer")
        #
        # payment = Payments.objects.create(user=user, course=paid_course, amount="30000",
        #                                  method="TRANSFER")
        # payment.save()

