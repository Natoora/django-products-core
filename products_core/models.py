import uuid
from django.db import models


class Status(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    DISABLED = 'DISABLED', 'Disabled'
    DISCONTINUED = 'DISCONTINUED', 'Discontinued'


class ProductCore(models.Model):

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, db_index=True)
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
    ACTIVE = 'ACTIVE'
    DISABLED = 'DISABLED'
    DISCONTINUED = 'DISCONTINUED'

    PRODUCT_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
        (DISCONTINUED, 'Discontinued'),
    )

    status = models.CharField(max_length=20, choices=PRODUCT_STATUS_CHOICES, default=ACTIVE)
    name = models.CharField(max_length=100, unique=True)
    uuid_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True
