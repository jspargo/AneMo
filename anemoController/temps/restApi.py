from temps.models import RecordedTemp, SetTemp, TempManager
from rest_framework import routers, serializers, viewsets
import datetime


# Thermostate Get all Temps Endpoint
class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordedTemp
        fields = ('recorded_temp', 'recorded_date')

class TempViewSet(viewsets.ModelViewSet):
    queryset = RecordedTemp.objects.all()
    serializer_class = TempSerializer


# Thermostate Get Latest Temps Endpoint
class GetLatestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordedTemp
        fields = ('recorded_temp', 'recorded_date')

class GetLatestViewSet(viewsets.ModelViewSet):
    # queryset = RecordedTemp.objects.latest()
    five_mins_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    queryset = RecordedTemp.objects.filter(recorded_date__gte=five_mins_ago)
    serializer_class = GetLatestSerializer


# Thermostate Set (Temps) Endpoint
class SetTempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SetTemp
        fields = ('set_temp_low', 'set_temp_high', 'set_date')

class SetTempViewSet(viewsets.ModelViewSet):
    queryset = SetTemp.objects.all()
    serializer_class = SetTempSerializer


# Thermostate State Endpoint
class GetStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempManager
        # TODO: Remove 'recorded_temp' and 'requested_temp'
        fields = ('state_date', 'return_state', 'override_state', 'recorded_temp', 'requested_temp')

class GetStateViewSet(viewsets.ModelViewSet):
    serializer_class = GetStateSerializer
    queryset = TempManager.objects.all()
