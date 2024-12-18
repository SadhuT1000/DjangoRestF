from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.all()


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter]
    filterset_fields = ['data', 'paid_course', 'paid_lesson', 'payment_method', ]
    ordering_fields = ['data', ]




