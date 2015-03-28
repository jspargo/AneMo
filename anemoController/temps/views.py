from django.shortcuts import render
from django.http import HttpResponse
from temps.models import RecordedTemp, SetTemp

import json

# Create your views here.

def index(request):
    if request.method=='POST':
        p = Payload(request.body)
        temp = p.temperature
        date = p.time

        #import pdb; pdb.set_trace()

        new_record = RecordedTemp(recorded_temp=temp, recorded_date=date)
        new_record.save()

        return HttpResponse('Success!  temp: ' + str(new_record.id) + ' ' + str(new_record.recorded_temp))
    return HttpResponse('POST method only')


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
