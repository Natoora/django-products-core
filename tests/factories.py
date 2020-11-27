from tests.models import ProductCore
from products_core.factories import ProductCoreFactory
from factory.fuzzy import FuzzyInteger


class ProductFactory(ProductCoreFactory):
    class Meta:
        model = ProductCore

    custom_attrib = FuzzyInteger(0, 100)
