from django.contrib import admin

from payment.models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
