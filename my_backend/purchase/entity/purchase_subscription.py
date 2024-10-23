from django.db import models

from purchase.entity.purchase import Purchase
from subscription.entity.subscription import Subscription


class PurchaseSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, related_name='purchase_subscription', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"PurchaseSubscription {self.id} for Purchase {self.purchase.id}"

    class Meta:
        db_table = 'purchase_subscription'
        app_label = 'purchase'
