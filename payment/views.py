from payment.models import Payment
from payment.serializers import PaymentSerializer

from rest_framework import viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
