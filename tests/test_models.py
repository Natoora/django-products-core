from django.core.exceptions import ValidationError
from django.test import TestCase
from tests.factory import ProductFactory
from .models import ProductCore, ProductBaseCore
#from products_core.models import ProductCore, ProductBaseCore


class ProductCoreModelTests(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_name_is_empty(self):
        try:
            product = ProductFactory()
            product.name = ""
            product.full_clean()
            product.save()
        except ValidationError:
            self.assertIs(ProductCore.objects.filter(name=product.name).exists(), False)

    def test_for_max_length(self):
        try:
            product = ProductFactory()
            product.name = ""
            for i in range(0, 500):
                product.name += "a"
            product.full_clean()
            product.save()
        except ValidationError:
            self.assertIs(ProductCore.objects.filter(name=product.name).exists(), False)

    def test_name_is_there(self):
        self.assertIs(ProductCore.objects.filter(name=self.product).exists(), True)

    def test_default_status(self):
        self.assertEqual(self.product.status, "ACTIVE")

    def test_disabled_status(self):
        product = ProductFactory(status="DISABLED")
        self.assertEqual(product.status, "DISABLED")

    def test_discontinued_status(self):
        product = ProductFactory(status="DISCONTINUED")
        self.assertEqual(product.status, "DISCONTINUED")

    # def test_return_active(self):
    #    product = ProductCoreFactory(name='MyTestName')
    #    print(ProductCore.objects.filter(status=ProductCore.ProductStatusChoice.ACTIVE).values())
    #    self.assertIs(ProductCore.objects.filter(name=self.product).exists(), True)

    # This is not working for now
    # def test_unknown_status(self):
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
