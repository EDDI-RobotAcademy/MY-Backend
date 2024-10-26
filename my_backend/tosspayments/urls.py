from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tosspayments.controller.views import TosspaymentsView

router = DefaultRouter()
router.register(r'tosspayments', TosspaymentsView, basename='tosspayments')

urlpatterns = [
    path('', include(router.urls)),
    path('create-payment', TosspaymentsView.as_view({'post': 'create_payment'}), name='create-payment'),
    path('payment-success', TosspaymentsView.as_view({'post': 'payment_success'}), name='payment-success'),
]
