from django.db import models
from products_core.models import ProductCore, ProductBaseCore


class ProductCore(ProductCore):
    custom_att = models.IntegerField()


class ProductBaseCore(ProductBaseCore):
    custom_att = models.IntegerField()
