from django.conf.urls import patterns, include, url

from novels.views import MainListView, MainDetailView, subscribe_to, IndexView, download_issue_archive, ReadOnlineView 
from novels.models import Group, Character, Publisher, Arc, Title, Issue, Strip

urlpatterns = patterns('',
#Index:
    url(r'^$', IndexView.as_view(), name='index'),
#Publisher:    
    url(r'^publishers/$', MainListView.as_view(model = Publisher, template_name = "novels/pub_list.html"), name='PublisherList'),
    url(r'^publishers/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Publisher, template_name = "novels/pub_detail.html"), name='PublisherDetail'),
    url(r'^subscribe/publisher/$', subscribe_to, {'mod': Publisher}, name='Sub_to_Pub'),
#Title:                       
    url(r'^titles/$', MainListView.as_view(model = Title, template_name = "novels/tit_list.html"), name='TitleList'),
    url(r'^titles/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Title, template_name = "novels/tit_detail.html"), name='TitleDetail'),
    url(r'^subscribe/title/$', subscribe_to, {'mod': Title}, name='Sub_to_Title'),
#Arc:
    url(r'^arcs/$', MainListView.as_view(model = Arc, template_name = "novels/arc_list.html"), name='ArcList'),
    url(r'^arcs/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Arc, template_name = "novels/arc_detail.html"), name='ArcDetail'),
    url(r'^subscribe/arc/$', subscribe_to, {'mod': Arc}, name='Sub_to_Arc'),
#Issue
    url(r'^titles/issue/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Issue, template_name = "novels/issue_detail.html"), name='IssueDetail'),
    url(r'^download/issue/(?P<pk>\d+)/$', download_issue_archive, name='Download_Issue'),
#Group:
    url(r'^groups/$', MainListView.as_view(model = Group, template_name = "novels/group_list.html"), name='GroupList'),
    url(r'^groups/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Group, template_name = "novels/group_detail.html"), name='GroupDetail'),
    url(r'^subscribe/group/$', subscribe_to, {'mod': Group}, name='Sub_to_Group'),
#Character:
    url(r'^chars/$', MainListView.as_view(model = Character, template_name = "novels/char_list.html"), name='CharList'),
    url(r'^chars/(?P<slug>[\w-]+)/$', MainDetailView.as_view(model = Character, template_name = "novels/char_detail.html"), name='CharDetail'),
    url(r'^subscribe/char/$', subscribe_to, {'mod': Character}, name='Sub_to_Char'),
#OnlineReading
    url(r'^read/(?P<title_slug>[\w-]+)/(?P<issue_slug>[\w-]+)/(?P<page>[0-9]+)/$', ReadOnlineView.as_view(model = Strip, template_name = "novels/read_strip.html"), name='ReadStrip'),
    )