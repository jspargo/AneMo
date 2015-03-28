from django.db import models

import json, datetime

# Create your models here.

class TempManager(models.Manager):
	def current_temp_within_range(self):
		#TODO: here we will compare latest recorded temp with set temps
	  	return True


class RecordedTemp(models.Model):
    recorded_temp = models.DecimalField(max_digits=5, decimal_places=2)
    recorded_date = models.DateTimeField('date recorded')

    objects = TempManager()

    def __unicode__(self):
    	temp = float(self.recorded_temp)
    	date = str(self.recorded_date)
        return u'%f -- %s' % (temp, date)

    def was_recorded_today(self):
        return self.recorded_date >= timezone.now() - datetime.timedelta(days=1)


class SetTemp(models.Model):
    set_temp_low = models.DecimalField(max_digits=5, decimal_places=2)
    set_temp_high = models.DecimalField(max_digits=5, decimal_places=2)
    set_date = models.DateTimeField('date set')

    def __unicode__(self):
    	temp_low = float(self.set_temp_low)
    	temp_high = float(self.set_temp_high)
    	date = str(self.set_date)
        return u'%f to %f -- %s' % (temp_low, temp_high, date)


class TimeConversion(str):
	def __str__(self):
		output = datetime.datetime.strptime(self, '%a, %d %b %Y %H:%M:%S GMT').strftime('%Y-%m-%d')
		return output
