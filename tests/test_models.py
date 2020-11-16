from django.core.exceptions import ValidationError
from django.test import TestCase
from tests.factory import ProductFactory
from .models import Product
from products_core.models import ProductCore, ProductBaseCore


class ProductCoreModelTests(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_name_is_empty(self):
        try:
            product = ProductFactory()
            product.name = ""
            product.full_clean()
            product.save()
        except:
            self.assertIs(Product.objects.filter(name=product.name).exists(), False)

    def test_for_max_length(self):
        try:
            product = ProductFactory()
            product.name = "Mihai1234123"
            for i in range(0, 500):
                product.name += "a"
            product.full_clean()
            product.save()
        # self.assertEqual(Product.name,'Ang')
        except ValidationError:
            self.assertIs(Product.objects.filter(name=product.name).exists(), False)
        except:
            print("Found Something Else")

    def test_name_is_there(self):
        #product = ProductFactory()
        self.assertIs(Product.objects.filter(name=self.product).exists(), True)
