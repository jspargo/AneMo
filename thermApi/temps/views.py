from django.shortcuts import render
from temps.models import currentTemp


def index(request):
    latest_temp = currentTemp.objects.order_by('-temp_timestamp')[:3]
    context = {'latest_temp': latest_temp}
    return render(request, 'temps/index.html', context)