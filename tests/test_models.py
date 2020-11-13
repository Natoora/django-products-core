from django.test import TestCase
from products_core.models import ProductStatusChoice, ProductCore, ProductBaseCore
from .models import Product
from faker import Factory
import factory

faker = Factory.create()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = faker.name()


class ProductCoreModelTests(TestCase):
    def setUp(self):
        self.product = ProductFactory.create()

    def test_name_is_empty(self):
        p = Product()
        p.status = ProductStatusChoice.ACTIVE
        p.save()
        num_results = Product.objects.filter(name='').count()
        self.assertEqual(num_results, 1)

    def test_name_is_there(self):
        self.assertIs(Product.objects.filter(name=self.product).exits(), True)
