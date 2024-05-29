# from django.db.models import *
from django.db import models
# Create your models here.

class Item(models.Model):
    name = models.CharField("Name",max_length=100, unique=True)
    description = models.TextField("Description", null=True)
    price = models.IntegerField("Price")
    count = models.IntegerField("Count")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    discount = models.IntegerField("Discount", default=0)

    def __str__(self):
        return self.name
