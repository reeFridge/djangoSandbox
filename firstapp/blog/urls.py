from django.conf.urls import patterns, include, url

from blog.views import PostListView, PostDetailView, like

urlpatterns = patterns('',
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^likes/$', like, name='like'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^page/(?P<page>[0-9]+)/$', PostListView.as_view(), name='paginate_list'),
    url(r'^category/(?P<pk>\d+)/$', PostListView.as_view(categorised = True), name='Categorise_list'),
    url(r'^category/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', PostListView.as_view(categorised = True), name='list'),
)
