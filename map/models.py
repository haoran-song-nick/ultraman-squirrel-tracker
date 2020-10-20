from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Point(models.Model):
    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        unique=True,
        help_text=_('Unique Squirrel ID'),
    )
    Latitude = models.FloatField(
        help_text=_('Latitude'),
    )
    Longtitude = models.FloatField(
        help_text=_('Longtitude'),
    )