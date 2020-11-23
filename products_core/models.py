import uuid
from django.db import models
from django.db.models import Max

"""
def get_next_productbase_code():
    try:
        next_productbase_code = ProductBaseCore.objects.all().aggregate(Max('code'))
        pb_code = next_productbase_code['code__max'] + 1
    except:
        pb_code = 66
    return pb_code


def get_next_product_code():
    try:
        next_product_code = ProductCore.objects.all().aggregate(Max('code'))
        p_code = next_product_code['code__max'] + 1
    except:
        p_code = 66
    return p_code
"""
class ProductManager(models.Manager):
    def get_active_products(self):
        return super().filter(status=ProductCommon.ProductStatusChoice.ACTIVE)


class ProductCommon(models.Model):
    class ProductStatusChoice(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        DISABLED = "DISABLED", "Disabled"
        DISCONTINUED = "DISCONTINUED", "Discontinued"
        FROM_WS_CORE = "FROMWSCORE", "FROMWSCORE"

    objects = ProductManager()
    status = models.CharField(
        max_length=20,
        choices=ProductStatusChoice.choices,
        default=ProductStatusChoice.ACTIVE,
        db_index=True,
    )
    # uuid_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class ProductCore(ProductCommon):
    """
    ProductCore Abstract Model
    """

    name = models.CharField(max_length=100)
    code = models.IntegerField(default=get_next_product_code, editable=False, unique=True)

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
    code = models.IntegerField(default=get_next_productbase_code(), editable=False, unique=True)

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
