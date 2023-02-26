from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
    # on_delete=models.CASCADE - if specified type of ths object will be deleted then all associated object with this type will be deleted
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
