from django.test import TestCase
from products_core.models import ProductCore, ProductBaseCore


class ProductCoreModelTests(TestCase):

    def test_name_is_empty(self):
        p = ProductCore()
        p.name = ''
        p.status = ProductCore.ProductStatusChoice.ACTIVE
        p.full_clean()
        p.save()
        self.assertEqual(p.name,'Ang')
