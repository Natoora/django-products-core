from django.db import models
import uuid


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
    uuid_code = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)

    class Meta:
        abstract = True
