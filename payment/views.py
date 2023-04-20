from django_filters import rest_framework as filters

from payment.models import Payment
from payment.serializers import PaymentSerializer, PaySerializer

from rest_framework import viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['user', 'currency', 'reference_code']


class PayViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    http_method_names = ['PUT']
    serializer_class = PaySerializer
