from temps.models import RecordedTemp, SetTemp
from rest_framework import routers, serializers, viewsets


class TempSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = RecordedTemp
		fields = ('recorded_temp', 'recorded_date')


class TempViewSet(viewsets.ModelViewSet):
	queryset = RecordedTemp.objects.all()
	serializer_class = TempSerializer


class GetLatestViewSet(viewsets.ModelViewSet):
	queryset = RecordedTemp.objects.all()
	serializer_class = TempSerializer