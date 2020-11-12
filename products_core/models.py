import uuid
from django.db import models


class Status(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    DISABLED = 'DISABLED', 'Disabled'
    DISCONTINUED = 'DISCONTINUED', 'Discontinued'

class ProductCore(models.Model):

    name = models.CharField(max_Field=100)
    status = models.CharField(max_length=2, choices=Status.choices,default=Status.ACTIVE,db_index=True)
    uuid_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # This code below function is here for testing
    def __str__(self):
        return self.name

    class Meta:
        abstract = True
