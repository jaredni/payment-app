from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    name = models.CharField(blank=True, max_length=45)
    code = models.CharField(blank=True, max_length=45, unique=True)
    created_date = models.DateField(auto_now_add=True)

class Payment(models.Model):
    user = models.ForeignKey(
        User, related_name='payment', on_delete=models.CASCADE)
    reference_code = models.CharField(blank=True, max_length=45, unique=True)
    amount = models.FloatField()
    currency = models.ForeignKey(
        Currency, related_name='payment', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


