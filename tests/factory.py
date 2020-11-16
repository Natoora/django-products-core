from factory.django import DjangoModelFactory
from faker import Factory
from tests.models import ProductC

faker = Factory.create()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = ProductC

    name = faker.name()