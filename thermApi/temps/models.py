import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class currentTemp(models.Model):
    temp_timestamp = models.DateTimeField('date recorded')
    temp_val = models.DecimalField(default=0, max_digits=5, decimal_places=2)
