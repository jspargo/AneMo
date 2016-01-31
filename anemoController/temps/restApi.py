from temps.models import RecordedTemp, SetTemp
from rest_framework import routers, serializers, viewsets
import datetime


class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordedTemp
        fields = ('recorded_temp', 'recorded_date')


class TempViewSet(viewsets.ModelViewSet):
    queryset = RecordedTemp.objects.all()
    serializer_class = TempSerializer


class GetLatestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordedTemp
        fields = ('recorded_temp', 'recorded_date')


class GetLatestViewSet(viewsets.ModelViewSet):
    # queryset = RecordedTemp.objects.latest()
    five_mins_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    queryset = RecordedTemp.objects.filter(recorded_date__gte=five_mins_ago)
    serializer_class = GetLatestSerializer
