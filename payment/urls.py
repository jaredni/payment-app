from django.urls import include, path
from rest_framework import routers

from payment import views

router = routers.SimpleRouter()

router.register(r"payment", views.PaymentViewSet)
router.register(r"pay", views.PayViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
