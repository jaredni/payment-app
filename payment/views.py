from django_filters import rest_framework as filters

from payment.models import Payment
from payment.serializers import PaymentSerializer

from rest_framework import viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['user', 'currency', 'reference_code']
