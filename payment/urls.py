from django.urls import path, include

from payment import views

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'payment', views.PaymentViewSet)
router.register(r'pay', views.PayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
