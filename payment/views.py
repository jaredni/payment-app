from django_filters import rest_framework as filters

from payment.models import Payment
from payment.permissions import IsOwner
from payment.serializers import PaymentSerializer, PaySerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    http_method_names = ["get", "post"]
    serializer_class = PaymentSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["currency", "reference_code"]

    def get_queryset(self):
        current_user = self.request.user
        return self.queryset.filter(user=current_user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PayViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = Payment.objects.select_related("user", "currency").all()
    http_method_names = ["get", "put"]
    serializer_class = PaySerializer

    def list(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)
