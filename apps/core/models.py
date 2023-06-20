from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True