from uuid import uuid4
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Admin(User):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('Admin')
        verbose_name_plural = _('Admins')