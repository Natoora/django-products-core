from factory.django import DjangoModelFactory
from faker import Factory
from tests.models import ProductCore, ProductBaseCore

faker = Factory.create()


class ProductCoreFactory(DjangoModelFactory):
    class Meta:
        model = ProductCore

    name = faker.name()