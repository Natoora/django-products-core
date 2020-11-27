from factory.django import DjangoModelFactory
from tests.models import ProductCore
import factory
import random


class ProductCoreFactory(DjangoModelFactory):
    class Meta:
        model = ProductCore

    status = random.choice(ProductCore.PRODUCT_STATUS_CHOICES)
    name = factory.Faker("name")
