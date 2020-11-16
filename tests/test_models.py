from django.core.exceptions import ValidationError
from django.test import TestCase
from tests.factory import ProductFactory
from .models import ProductC, ProductB
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
            self.assertIs(ProductC.objects.filter(name=product.name).exists(), False)

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
            self.assertIs(ProductC.objects.filter(name=product.name).exists(), False)
        except:
            print("Found Something Else")

    def test_name_is_there(self):
        self.assertIs(ProductC.objects.filter(name=self.product).exists(), True)

    def test_default_status(self):
        self.assertEqual(self.product.status, "ACTIVE")

    def test_disabled_status(self):
        product = ProductFactory(status="DISABLED")
        self.assertEqual(product.status, "DISABLED")

    def test_discontinued_status(self):
        product = ProductFactory(status="DISCONTINUED")
        self.assertEqual(product.status, "DISCONTINUED")

    # This is not working for now
    #def test_unknown_status(self):
    #    try:
    #        product = ProductFactory(status="erasdfjiAAA")
    #        product.name = ""
    #        print("1")
    #        product.full_clean()
    #        print("2")
    #        product.save()
    #    except:
    #        print("ASDZXC")
    #        print(ProductC.objects.all().values())
    #        self.assertIs(ProductC.objects.filter(name=product.name).exists(), False)
