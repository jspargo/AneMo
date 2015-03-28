from django.conf.urls import patterns, url

from temps import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)