from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from temps.restApi import TempViewSet, GetLatestViewSet, SetTempViewSet, GetStateViewSet, SetTimeViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'temp', TempViewSet)
router.register(r'latest', GetLatestViewSet)
router.register(r'set', SetTempViewSet)
router.register(r'state', GetStateViewSet)
router.register(r'times', SetTimeViewSet)


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^temps/', include('temps.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       )
