from django_filters import rest_framework as filters

from payment.models import Payment
from payment.serializers import PaymentSerializer, PaySerializer

from rest_framework import viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = PaymentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['user', 'currency', 'reference_code']


class PayViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    http_method_names = ['get', 'put']
    serializer_class = PaySerializer

    def list(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)
