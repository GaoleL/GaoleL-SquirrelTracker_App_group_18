from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.forms import ModelForm

class Meta:
    managed = True

class squirrel(models.Model):
    X = models.FloatField(
            help_text=_('Longitude'),
            )
    Y = models.FloatField(
        help_text=_('Latitude'),
        )
    Unique_squirrel_id = models.CharField(
        max_length=100,
        help_text=_('Unique Squirrel ID'),
        )
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES =(
            (AM,'AM'),
            (PM,'PM'),
            )
    Shift  = models.CharField(
         max_length=100,
         choices = SHIFT_CHOICES,
         help_text=_('Shift Choices'),
         )
    Date = models.DateField(
            help_text=_('Date'),
            )
    AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            )
    Age = models.CharField(
            max_length=100,
            choices=AGE_CHOICES,
            blank = True,
            )
    COLOR_CHOICES = ((GREY,'Grey'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
            )
    Primary_Fur_Color = models.CharField(
            help_text=_('Primary Fur Color'),
            max_length=100,
            choices=COLOR_CHOICES,
            blank = True,
            )
    LOCATION_CHOICES =(
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
            )
    Location = models.CharField(
            max_length=100,
            choices = LOCATION_CHOICES,
            blank=True,
            help_text=_('location'),
    )
    Specific_location=models.CharField(
            max_length=100,
            help_text=_('Specific Location'),
            blank = True,
            )
    Running = models.BooleanField(
            max_length = 100,
            help_text=_('running'),
            )
    Chasing = models.BooleanField(
            max_length = 100,
            help_text=_('chasing'),
            )
    Climbing = models.BooleanField(
            max_length = 100,
            help_text=_('climbing'),
            )
    Eating = models.BooleanField(
            max_length = 100,
            help_text=_('eating'),
            )
    Foraging = models.BooleanField(
            max_length = 100,
            help_text=_('foraging'),
            )
    Other_activities = models.CharField(
            max_length=100,
            blank=True,
            help_text=_('other activities'),
    )
    Kuks = models.BooleanField(
            max_length = 100,
            help_text=_('kukking'),
            )
    Quaas = models.BooleanField(
            max_length = 100,
            help_text=_('quaaing'),
            )
    Moans = models.BooleanField(
            max_length = 100,
            help_text=_('moaning'),
            )
    Tail_flags = models.BooleanField(
            max_length = 100,
            help_text=_('Tail flagging'),
            )
    Tail_twitches = models.BooleanField(
            max_length = 100,
            help_text=_('Tail twitching'),
            )
    Approaches = models.BooleanField(
            max_length = 100,
            help_text=_('approaching')
            )
    Indifferent = models.BooleanField(
            max_length = 100,
            help_text=_('indifferent'),
            )
    Runs_From = models.BooleanField(
            max_length = 100,
            help_text=_('running from humans'),
            )



# Create your models here.
