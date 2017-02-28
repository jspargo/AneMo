from django.db import models

import json, datetime
import logging

# Create your models here.

class RecordedTemp(models.Model):
    recorded_temp = models.DecimalField(max_digits=5, decimal_places=2)
    recorded_date = models.DateTimeField('date recorded')

    class Meta:
        get_latest_by = 'recorded_date'
        ordering = ['-recorded_date']

    def __unicode__(self):
        temp = float(self.recorded_temp)
        date = str(self.recorded_date)
        return u'%f' % (temp)

    def was_recorded_today(self):
        return self.recorded_date.date() >= timezone.now() - datetime.timedelta(days=1)


class SetTemp(models.Model):
    set_temp_low = models.DecimalField(max_digits=5, decimal_places=2)
    set_temp_high = models.DecimalField(max_digits=5, decimal_places=2)
    set_date = models.DateTimeField('date set')

    class Meta:
        get_latest_by = 'set_date'
        ordering = ['-set_date']

    def __unicode__(self):
        temp_low = float(self.set_temp_low)
        temp_high = float(self.set_temp_high)
        date = str(self.set_date)
        return u'%f to %f -- %s' % (temp_low, temp_high, date)


class TimeConversion(str):
    def __str__(self):
        output = datetime.datetime.strptime(self, '%a, %d %b %Y %H:%M:%S GMT').strftime('%Y-%m-%d')
        return output


class TempManager(models.Model):
    recorded_temp = models.DecimalField(max_digits=5, decimal_places=2)
    requested_temp = models.DecimalField(max_digits=5, decimal_places=2)
    logic_state = models.BooleanField(default=False)
    override_state = models.BooleanField(default=False)
    state_date = models.DateTimeField('state date')

    def calculate_state_logic(self):
        "Using Temps and Dates, establish logic state to return"
        if self.recorded_temp < self.requested_temp:
            logging.warning('%f is less than %f - heating state set to ON', self.recorded_temp, self.requested_temp)
            return True
        else:
            logging.warning('%f is greater than %f - heating state set to OFF', self.recorded_temp, self.requested_temp)
            return False

    def _get_state_to_return(self):
        "Returns state (overridden or logic)"
        if self.override_state is True:
            return True
        else:
            return self.calculate_state_logic

    def _get_latest_temp(self):
        latest_temp = RecordedTemp.objects.latest().recorded_temp
        #logging.warning('Latest Recorded Temp: %f', latest_temp)
        return latest_temp

    def _get_latest_set_temp(self):
        latest_set_temp = SetTemp.objects.latest().set_temp_high
        #logging.warning('Requested Temp: %f', latest_set_temp)
        return latest_set_temp

    recorded_temp = property(_get_latest_temp)
    requested_temp = property(_get_latest_set_temp)
    return_state = property(_get_state_to_return)

    class Meta:
        ordering = ['-state_date']

    def __unicode__(self):
        temp = float(self.recorded_temp)
        date = str(self.state_date)
        state = bool(self.return_state)

        return u'%f so state is %b -- %s' % (temp, state, date)


class SetTimes(models.Model):
    time_set_date = models.DateTimeField('date time set')
    set_first_time= models.DateTimeField('morning on time')
    set_second_time = models.DateTimeField('morning off time')
    set_third_time = models.DateTimeField('afternoon on time')
    set_fourth_time = models.DateTimeField('afternoon off time')

    class Meta:
        get_latest_by = 'time_set_date'
        ordering = ['-time_set_date']

    def __unicode__(self):
        temp_low = float(self.set_temp_low)
        temp_high = float(self.set_temp_high)
        date = str(self.set_date)
        return u'%f to %f -- %s' % (temp_low, temp_high, date)
