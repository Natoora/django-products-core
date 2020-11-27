from tests.models import Product, ProductBase
from products_core.factories import ProductCoreFactory, ProductBaseCoreFactory
from factory.fuzzy import FuzzyInteger


class ProductBaseCoreFactory(ProductBaseCoreFactory):
    class Meta:
        model = ProductBase

    custom_attrib = FuzzyInteger(0, 100)


class ProductCoreFactory(ProductCoreFactory):
    class Meta:
        model = Product

    custom_attrib = FuzzyInteger(0, 100)

