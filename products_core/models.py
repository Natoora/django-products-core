import uuid
from django.db import models


class ProductStatusChoice(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    DISABLED = 'DISABLED', 'Disabled'
    DISCONTINUED = 'DISCONTINUED', 'Discontinued'


class ProductCore(models.Model):
    """
    ProductCore Abstract Model
    """
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=ProductStatusChoice.choices,
                              default=ProductStatusChoice.ACTIVE, db_index=True)
    uuid_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # This code below function is here for testing
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class ProductBaseCore(models.Model):
    """
    ProductBaseCore Abstract Model
    """
    status = models.CharField(max_length=20, choices=ProductStatusChoice.choices,
                              default=ProductStatusChoice.ACTIVE, db_index=True)
    name = models.CharField(max_length=100, unique=True)
    uuid_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

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

# Questions:
# 1. Do we need to use the same list of choices for both statuses in the 2 classes?
# 2. If no, do we use the tuple in the ss for the ProductBaseCore
# 3. If yes, can we not inherit the fields from ProductCore in ProductBaseCore ? (use only 1 class?)
