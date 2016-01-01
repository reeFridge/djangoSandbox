from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', MtgListView.as_view(), name='index'),
)