from factory.django import DjangoModelFactory
from tests.models import ProductCore, ProductBaseCore
import factory
import random


class ProductCoreFactory(DjangoModelFactory):
    class Meta:
        model = ProductCore

    status = random.choice(ProductCore.PRODUCT_STATUS_CHOICES)
    name = factory.Faker("name")


class ProductBaseCoreFactory(DjangoModelFactory):
    class Meta:
        model = ProductBaseCore

    status = random.choice(ProductCore.PRODUCT_STATUS_CHOICES)
    name = factory.Faker("name")
