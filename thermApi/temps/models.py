import datetime

from django.utils import timezone
from django.db import models
from temps import thermostat

# Create your models here.

class currentTemp(models.Model):
    temp_timestamp = models.DateTimeField('date recorded')
    temp_val = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __unicode__(self):
        temp_string = str(self.temp_val)
        return temp_string
    
    def was_recorded_recently(self):
        return self.temp_timestamp >= timezone.now() - datetime.timedelta(days=1)
    was_recorded_recently.admin_order_field = 'temp_timestamp'
    was_recorded_recently.boolean = True
    was_recorded_recently.short_description = 'Temp recorded recently?'