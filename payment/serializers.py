from django.db.models import Sum
from django.utils import timezone
from rest_framework import serializers

from payment.constants import DAILY_LIMIT
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(source="currency", read_only=True)
    username = serializers.CharField(source="user", read_only=True)

    @staticmethod
    def get_total_amount(user, currency, amount):
        date_now = timezone.now().date()

        total = Payment.objects.filter(
            user=user.pk, currency=currency.pk, created_date__icontains=date_now
        ).aggregate(total=Sum("amount"))["total"]

        if total is None:
            total = 0
        return total + amount

    def validate(self, attrs):
        request = self.context["request"]
        total = self.get_total_amount(
            request.user, attrs.get("currency"), attrs.get("amount")
        )

        if total > DAILY_LIMIT:
            raise serializers.ValidationError("5000 daily limit reached")

        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["is_paid"] = instance.is_paid
        data["date_paid"] = instance.paid_date

        return data

    class Meta:
        model = Payment
        exclude = ("is_paid", "paid_date", "user")


class PaySerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        validated_data["paid_date"] = timezone.now().date()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["amount"] = instance.amount
        data["user"] = instance.user.username
        data["currency_code"] = instance.currency.code

        return data

    class Meta:
        model = Payment
        fields = ["id", "is_paid"]
