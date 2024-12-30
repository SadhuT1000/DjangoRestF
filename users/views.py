# flake8: noqa

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.serializers import PaymentSerializer, UserSerializer
from users.services import create_price, create_link, create_product

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="Просмотр списка пользователей"
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Создание пользователя"
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="Просмотр пользователя"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Удаление пользователя"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Обновление пользователя"
))



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.all()


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        "data",
        "paid_course",
        "paid_lesson",
        "payment_method",
    ]
    ordering_fields = [
        "data",
    ]


class PaymentsCreateApiView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        price = create_price(payment.amount)
        session_id, payment_link = create_link(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()







class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
