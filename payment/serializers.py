from django.db.models import Sum
from django.utils import timezone

from payment.constants import DAILY_LIMIT
from payment.models import Payment

from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(source='currency')
    username = serializers.CharField(source='user')

    @staticmethod
    def get_total_amount(user, currency, amount):
        now = timezone.now().date()

        total = Payment.objects.filter(
            user=user, currency=currency, created_date=now).aggregate(
            total=Sum('amount'))['total']

        return total + amount

    def validate(self, attrs):
        total = self.get_total_amount(
            attrs.get('user'), attrs.get('currency'), attrs.get('amount'))
        if total >  DAILY_LIMIT:
            raise serializers.ValidationError('5000 daily limit reached')

        super().validate(attrs)

    class Meta:
        model = Payment
        fields = '__all__'


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'is_paid']

    def update(self, instance, validated_data):
        validated_data['paid_date'] = timezone.now().date()
        return super().update(instance, validated_data)
