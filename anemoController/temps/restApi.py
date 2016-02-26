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
    queryset = RecordedTemp.objects.order_by('-recorded_date')[:1]
    serializer_class = GetLatestSerializer
