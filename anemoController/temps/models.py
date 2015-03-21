from django.db import models

# Create your models here.

class RecordedTemp(models.Model):
    recorded_temp = models.DecimalField(max_digits=5, decimal_places=2)
    recorded_date = models.DateTimeField('date recorded')

    def __unicode__(self):
    	temp = float(self.recorded_temp)
    	date = str(self.recorded_date)
        return u'%f - %s' % (temp, date)


class SetTemp(models.Model):
    set_temp = models.DecimalField(max_digits=5, decimal_places=2)
    set_date = models.DateTimeField('date set')

    def __unicode__(self):
    	temp = float(self.set_temp)
    	date = str(self.set_date)
        return u'%f - %s' % (temp, date)