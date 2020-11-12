from django.db import models
from products_core.models import ProductCore


class Product(ProductCore):
    custom_att = models.CharField(max_length=200)
