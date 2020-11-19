from tests.models import ProductCore, ProductBaseCore
from products_core.factories import ProductCoreFactory
from factory.fuzzy import FuzzyInteger


class ProductFactory(ProductCoreFactory):
    class Meta:
        model = ProductCore

    custom_att = FuzzyInteger(0, 100)
