from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from tests.factory import ProductCoreFactory
import random
import string
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('products.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ProductCoreModelTests(TestCase):
    """ Product Core TestCases """

    def setUp(self):
        self.product = ProductCoreFactory(name="foobar", uuid_code="c532c472-cb23-4c91-994e-36ca1da8b71e")
        logger.info('Finished setUp: Created ProductCore object: {} - {}'.format(self.product.name, self.product.status))

    #
    # Attributes from Abstract Model
    #

    # name
    def test_name(self):
        logger.info('Doing the test_name test')
        self.assertEqual(self.product.name, "foobar")

    def test_name_max_length(self):
        logger.info('Doing the test_name_max_length test')
        exceed_limits = "".join(
            random.choices(string.ascii_letters + string.digits, k=201)
        )
        with self.assertRaises(ValidationError):
            self.product.name = exceed_limits
            self.product.full_clean()  # calls save()

    def test_name_not_null(self):
        logger.info('Doing the test_name_not_null test')
        with self.assertRaises(ValidationError):
            self.product.name = None
            self.product.full_clean()  # calls save()

    # status
    def test_status(self):
        self.assertEqual(self.product.status, self.product.ProductStatusChoice.ACTIVE)

    def test_unknown_status(self):
        with self.assertRaises(ValidationError):
            self.product.status = "NOT_IN_THE_CHOICES"
            self.product.full_clean()  # calls save()

    def test_status_max_length(self):
        # Not possible to test as it is not a valid choice.
        pass

    def test_status_default(self):
        product = ProductCoreFactory()
        product.name = "foo"
        product.save()
        self.assertEquals(product.status, product.ProductStatusChoice.ACTIVE)

    def test_status_not_null(self):
        with self.assertRaises(IntegrityError):
            ProductCoreFactory.create(status=None)

    # uuid_code
    def test_uuid_code(self):
        self.assertEqual(
            self.product.uuid_code, "c532c472-cb23-4c91-994e-36ca1da8b71e"
        )

    def test_uuid_code_is_not_editable(self):
        # Not possible to test as editable=False only applies to Django Admin
        pass

    def test_uuid_code_unique(self):
        with self.assertRaises(IntegrityError):
            ProductCoreFactory.create(uuid_code="c532c472-cb23-4c91-994e-36ca1da8b71e")

    def test_uuid_code_not_null(self):
        with self.assertRaises(IntegrityError):
            ProductCoreFactory.create(uuid_code=None)
