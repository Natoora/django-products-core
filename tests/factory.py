from factory.django import DjangoModelFactory
from faker import Factory
from tests.models import Product

faker = Factory.create()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = faker.name()