from django.db import models

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    type = models.CharField(max_length=128, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscription'