from django.test import TestCase
from products_core.models import ProductStatusChoice, ProductCore, ProductBaseCore
from .models import Product


class ProductCoreModelTests(TestCase):

    def test_name_is_empty(self):
        p = Product()
        p.name = 'Mihai'
        p.status = ProductStatusChoice.ACTIVE
        p.save()
        self.assertEqual(p.name, 'Mihai')
