from .models import ProductCore
from django.test import TestCase


class test_case_1(TestCase):
    def tes_2(self):
        status = ProductCore.ProductStatusChoice.ACTIVE
