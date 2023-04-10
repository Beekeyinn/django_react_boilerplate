from uuid import uuid4

from django.db import models


class ExtraFieldsModelsMixin(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
