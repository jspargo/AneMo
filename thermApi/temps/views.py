from django.shortcuts import render
from temps.models import currentTemp
from django.core import serializers


def index(request):
    latest_temp = currentTemp.objects.order_by('-temp_timestamp')[:3]
    #context = {'latest_temp': latest_temp}
    #return render(request, 'temps/index.html', context)
    serialized_obj = serializers.serialize('json', [ latest_temp, ])
    return serialized_obj

def current(request):
    latest_temp = currentTemp.objects.order_by('-temp_timestamp')[:1]
    context = {'latest_temp': latest_temp}
    return render(request, 'temps/index.html', context)