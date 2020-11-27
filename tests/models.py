from django.db import models
from products_core.models import ProductCore, ProductBaseCore


# TODO change it to ProductBase
class ProductBaseCore(ProductBaseCore):
    custom_attrib = models.IntegerField()


# TODO change it to Product
class ProductCore(ProductCore):
    custom_attrib = models.IntegerField(default=123)
    # TODO create link with ProductBase

