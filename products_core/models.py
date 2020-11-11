from django.db import models
import uuid


class ProductsCore(models.Model):
    Active = 'Active'
    name = models.CharField(max_Field=100)
    status = models.CharField(max_Field=20)
    # id = models.UUIDField(primary_key=Tr)
    abstract = True
