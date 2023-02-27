from django.db import models
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    title = models.CharField(max_length=255)
    date_delivery = models.DateField()
    quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
    # on_delete=models.CASCADE - if specified type of ths object will be deleted then all associated object with this type will be deleted
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    # default=timezone.now() - if use 'now()' as method - date time will be hardcoded during migration. To be more dunamic use as ref to method 'now()'
    date_created = models.DateTimeField(default=timezone.now)
