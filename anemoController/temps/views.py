from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

import json

# Create your views here.

def index(request):
    if request.method=='POST':
        p = Payload(request.body)
        temp = p.temperature
        date = p.time
        str_temp = '<br>temp: <b>' + str(temp) + '</b>'
        str_date = '<br>date: <b>' + str(date) + '</b>'
        return HttpResponse('Success!  temp: ' + str_date + str_temp)
    return HttpResponse('POST method only')


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)