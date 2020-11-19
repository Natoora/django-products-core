from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from tests.models import ProductCore, ProductBaseCore
import factory

class ProductCoreFactory(DjangoModelFactory):
    class Meta:
        model = ProductCore

    status = FuzzyChoice(CustomerCore.StatusChoices)
    name = factory.Faker("name")
