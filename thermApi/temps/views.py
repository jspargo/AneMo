from django.shortcuts import render
from temps.models import currentTemp
from django.core import serializers


def index(request):
    obj = currentTemp.objects
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, mimetype='application/json')

def current(request):
    latest_temp = currentTemp.objects.order_by('-temp_timestamp')[:1]
    context = {'latest_temp': latest_temp}
    return render(request, 'temps/index.html', context)