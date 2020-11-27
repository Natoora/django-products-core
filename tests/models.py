from django.db import models
from products_core.models import ProductCore, ProductBaseCore


class ProductBase(ProductBaseCore):
    custom_attrib = models.IntegerField()


class Product(ProductCore):
    custom_attrib = models.IntegerField(default=123)



