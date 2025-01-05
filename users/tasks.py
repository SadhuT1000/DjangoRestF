from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from users.models import User

from datetime import datetime, timedelta

@shared_task
def block_user():
    """Заблокировать пользователей, не активных в течение месяца"""
    month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=month_ago, is_active=True)
    inactive_users.update(is_active=False)