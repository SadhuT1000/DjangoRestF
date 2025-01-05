from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER



@shared_task
def send_information_about_update(email, message):
    """Отправляет пользователю уведомление о обновлении курса"""

    send_mail('ку-ку! вышло обновление курса', message, EMAIL_HOST_USER, [email])
