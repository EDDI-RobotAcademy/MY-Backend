from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscription.controller.views import SubscriptionView

router = DefaultRouter()
router.register(r'subscription', SubscriptionView, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('list', SubscriptionView.as_view({'get': 'listSubscription'}), name='list-subscription'),
    path('create', SubscriptionView.as_view({'post': 'createSubscription'}), name='create-subscription'),
    path('read', SubscriptionView.as_view({'post': 'readSubscription'}), name='read-subscription'),
]