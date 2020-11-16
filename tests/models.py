from django.db import models
from products_core.models import ProductCore, ProductBaseCore


class ProductCore(ProductCore):
    custom_att = models.CharField(max_length=200, default="123")


class ProductBaseCore(ProductBaseCore):
    custom_att = models.CharField(max_length=200, default="123")
