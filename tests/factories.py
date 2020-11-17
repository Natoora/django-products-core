from faker import Factory
from tests.models import ProductCore, ProductBaseCore
from products_core.factories import ProductCoreFactory

faker = Factory.create()


class ProductFactory(ProductCoreFactory):
    class Meta:
        model = ProductCore
