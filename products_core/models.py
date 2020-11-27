from django.db import models


class ProductCommon(models.Model):
    """
    ProductCommon Model contains attributes that are common between Product and ProductBase
    """

    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    DISCONTINUED = 'DISCONTINUED'

    PRODUCT_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
        (DISCONTINUED, 'Discontinued'),
    )

    status = models.CharField(
        max_length=20,
        choices=PRODUCT_STATUS_CHOICES,
        default=ACTIVE,
        db_index=True,
    )

    class Meta:
        abstract = True


class ProductCore(ProductCommon):
    """
    ProductCore Abstract Model
    """

    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductBaseCore(ProductCommon):
    """
    ProductBaseCore Abstract Model
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
