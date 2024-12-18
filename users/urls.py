from django.urls import path
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet
from config import settings
from django.conf.urls.static import static

app_name = UsersConfig.name

router = SimpleRouter()

router.register(r"", UserViewSet, basename='users')
router.register(r"payments", PaymentsViewSet, basename='payments')



urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)