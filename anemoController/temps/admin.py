from django.contrib import admin
from temps.models import RecordedTemp, SetTemp

# Register your models here.

admin.site.register(RecordedTemp)
admin.site.register(SetTemp)