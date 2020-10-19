from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
        help_text=_('Latitude'),
    )

    longitude = models.FloatField(
        help_text=_('Longitude'),
    ) 

    squirrel_id = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=256,
        primary_key=True
    )
    
    AM = 'AM'
    PM = 'PM'
    

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift'),
        max_length = 16,
        choices=SHIFT_CHOICES,
    )

    date = models.DateField(
        help_text=_('Date'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        help_text=_('Age'),
        max_length = 64,
        choices=AGE_CHOICES,
        null=True,
        blank=True,    
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )
    
    color = models.CharField(
         help_text=_('Primary Fur Color'),
         max_length = 64,
         choices=COLOR_CHOICES,
         null=True,
         blank=True,    
    )

    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND, 'Ground Plane'),
        (ABOVE, 'Above Ground'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=128,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
    )

    specific_location = models.CharField(
         help_text=_('Specific Location'),
         max_length=256,
         null=True,
         blank=True,
    )

    running = models.BooleanField(
         help_text=_('Running'),
    )

    chasing = models.BooleanField(
         help_text=_('Chasing'),
    )

    climbing = models.BooleanField(
         help_text=_('Climbing'),
    )
    
    eating = models.BooleanField(
         help_text=_('Eating'),
    )

    foraging = models.BooleanField(
         help_text=_('Foraging'),
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=256,
        null=True,
        blank=True,
    )

    kuks = models.BooleanField(
         help_text=_('Kuks'),
    )

    quaas = models.BooleanField(
         help_text=_('Quaas'),
    )

    moans = models.BooleanField(
         help_text=_('Moans'),
    )

    tail_flag = models.BooleanField(
         help_text=_('Tail flags'),
    )

    tail_twitches = models.BooleanField(
         help_text=_('Tail twitches'),
    )

    approaches = models.BooleanField(
         help_text=_('Approaches'),
    )

    indifferent = models.BooleanField(
         help_text=_('Indifferent'),
    )

    runs_from = models.BooleanField(
         help_text=_('Runs from'),
    )

    def __str__(self):
        return self.squirrel_id
# Create your models here.
