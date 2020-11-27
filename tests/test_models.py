from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from tests.factories import ProductCoreFactory
from tests.models import ProductCore
import random
import string


class ProductCoreModelTests(TestCase):
    """ Product Core TestCases """

    def setUp(self):
        # TODO create a product_base and link with product
        # self.product_base = TODO
        self.product = ProductCoreFactory.create(
            status=ProductCore.ACTIVE,
            name="foobar",
            custom_attrib=10,
        )

    #
    # Attributes from Abstract Model
    #

    # TODO remove it
    # uuid_code
    #def test_uuid_code(self):
    #    self.assertEqual(
    #        self.product.uuid_code, "c532c472-cb23-4c91-994e-36ca1da8b71e"
    #    )

    #def test_uuid_code_is_not_editable(self):
    #    # Not possible to test as editable=False only applies to Django Admin
    #    pass

    #def test_uuid_code_unique(self):
    #    with self.assertRaises(IntegrityError):
    #        ProductCoreFactory.create(
    #            uuid_code="c532c472-cb23-4c91-994e-36ca1da8b71e"
    #        )

    #def test_uuid_code_not_null(self):
    #    with self.assertRaises(IntegrityError):
    #        ProductCoreFactory.create(uuid_code=None)

    # status
    def test_status(self):
        self.assertEqual(
            self.product.status, self.product.ACTIVE
        )

    def test_unknown_status(self):
        with self.assertRaises(ValidationError):
            self.product.status = "NOT_IN_THE_CHOICES"
            self.product.full_clean()  # calls save()

    def test_status_max_length(self):
        # Not possible to test as it is not a valid choice.
        pass

    def test_status_default(self):
        product = ProductCore()
        product.name = "foo"
        product.save()
        self.assertEquals(product.status, product.ACTIVE)

    def test_status_not_null(self):
        with self.assertRaises(IntegrityError):
            ProductCoreFactory.create(status=None)

    # name
    def test_name(self):
        self.assertEqual(self.product.name, "foobar")

    def test_name_max_length(self):
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=201)
        )
        with self.assertRaises(ValidationError):
            self.product.name = exceed_limits
            self.product.full_clean()  # calls save()

    def test_name_not_null(self):
        with self.assertRaises(ValidationError):
            self.product.name = None
            self.product.full_clean()  # calls save()

    #
    # Attributes from Model
    #

    # custom_att
    def test_custom_attrib(self):
        self.assertEqual(self.product.custom_attrib, 10)

    def test_custom_attrib_null(self):
        with self.assertRaises(ValidationError):
            self.product.custom_attrib = None
            self.product.full_clean()  # calls save()

    #
    # Miscellaneous
    #
    def test_create_batch(self):
        ProductCoreFactory.create_batch(499)
        self.assertEquals(ProductCore.objects.count(), 500)  # 499 + setUp one
