from django.test import TestCase

from products_core.factory import ProductFactory


class ProductCoreModelTests(TestCase):
    def test_name_is_empty(self):
        product = ProductFactory()
        product.name = ""
        product.full_clean()
        product.save()
        # self.assertEqual(Product.name,'Ang')
        self.assertTrue(product.name)

    def test_for_max_length(self):
        product = ProductFactory()
        product.full_clean()
        product.save()
        # self.assertEqual(Product.name,'Ang')
        self.assertTrue(product.name)
