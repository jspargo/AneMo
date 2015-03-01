from django.db import models

# Create your models here.

class currentTemp(models.Model):
    temp_timestamp = models.DateTimeField('date recorded')
    temp_val = models.DecimalField(..., max_digits=5, decimal_places=2)