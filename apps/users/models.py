from django.db import models
from apps.core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

ROLE_CHOICES = (
    ("customer", "Customer"),
    ("admin", "Admin"),
    ("customer_service", "Customer Service"),
    ("restaurant", "Restaurant"),
)

class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=32, default="individual")

    def __str__(self):
        return self.username