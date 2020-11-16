from factory.django import DjangoModelFactory
from faker import Factory
from products_core.models import ProductCore

faker = Factory.create()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = ProductCore

    name = faker.name()
