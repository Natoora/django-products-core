from django.db import models


class ProductsCore(models.Model):
    name = models.CharField(max_Field = 100)
    status = models.CharField(max_Field = 20)
    abstract = True
