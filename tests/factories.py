from tests.models import ProductCore, ProductBaseCore
from products_core.factories import ProductCoreFactory


class ProductFactory(ProductCoreFactory):
    class Meta:
        model = ProductCore

     
