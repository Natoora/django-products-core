from django.db import models
import uuid


class ProductCore(models.Model):

    name = models.CharField(max_Field=100)
    status = models.CharField(max_Field=20)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
