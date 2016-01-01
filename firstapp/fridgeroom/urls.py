from django.conf.urls import patterns, include, url
from fridgeroom.views import PubsList, PubDetail

urlpatterns = patterns('',
    url(r'^$', PubsList.as_view(), name='list'),
    url(r'^pub/(?P<pk>\d+)/$', PubDetail.as_view(), name='detail'),    
)