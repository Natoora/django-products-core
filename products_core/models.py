import uuid
from django.db import models


def get_next_product_code():
    """
    Overriding this in the file that imports
    """
    pass

class ProductManager(models.Manager):
    def get_active_products(self):
        return super().filter(status=ProductCommon.ProductStatusChoice.ACTIVE)


class ProductCommon(models.Model):
    class ProductStatusChoice(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        DISABLED = "DISABLED", "Disabled"
        DISCONTINUED = "DISCONTINUED", "Discontinued"

    objects = ProductManager()
    code = models.IntegerField(default=get_next_product_code, editable=False, unique=True)
    status = models.CharField(
        max_length=20,
        choices=ProductStatusChoice.choices,
        default=ProductStatusChoice.ACTIVE,
        db_index=True,
    )
    #uuid_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class ProductCore(ProductCommon):
    """
    ProductCore Abstract Model
    """

    name = models.CharField(max_length=100)

    # This function is here for testing
    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ProductBaseCore(ProductCommon):
    """
    ProductBaseCore Abstract Model
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True

"""
    OLD STYLE TUPLE
    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    DISCONTINUED = 'DISCONTINUED'
    PRODUCT_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
        (DISCONTINUED, 'Discontinued'),
    )
"""
