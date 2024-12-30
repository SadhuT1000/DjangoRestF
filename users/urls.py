from django.conf.urls.static import static
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from config import settings
from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserCreateApiView, UserViewSet, PaymentsCreateApiView

app_name = UsersConfig.name

router = SimpleRouter()

router.register(r"", UserViewSet, basename="users")
router.register(r"payments", PaymentsViewSet, basename="payments")


urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("pay_course/", PaymentsCreateApiView.as_view(), name='pay_course'),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
