from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from novels.models import Group, Character, Publisher, Arc, Title, Issue, Strip
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.encoding import smart_str
import json
from django.http import HttpResponse
from datetime import datetime, timedelta

class MainListView(ListView):
    ''' empty '''
        
class ReadOnlineView(ListView):
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super(ReadOnlineView, self).get_context_data(**kwargs)
        issue = get_object_or_404(Issue, tit__slug = self.kwargs['title_slug'], slug=self.kwargs['issue_slug'])
        total_strip = Strip.objects.filter(issue=issue).count()
        progress = round((int(self.kwargs['page']) * 100)/total_strip)
        context['progress'] = progress
        context['issue'] = issue
        return context
        
    def get_queryset(self):
        obj = get_object_or_404(Issue, tit__slug = self.kwargs['title_slug'], slug=self.kwargs['issue_slug'])
        qset = Strip.objects.filter(issue=obj).order_by('num')
        return qset
    
    
class MainDetailView(DetailView):
    
    def get_context_data(self, **kwargs):
        context = super(MainDetailView, self).get_context_data(**kwargs)
        obj = super(MainDetailView, self).get_object()
        user = self.request.user
        if self.model == Publisher:
            subed = obj.subs.filter(id=user.id).exists()
            context['subed'] = subed
        if self.model == Title:
            issues = Issue.objects.filter(tit=obj)
            
            thumbnails = []
            for issue in issues:
                thumbnails.append(Strip.objects.get(issue=issue,num=0))
                
            context['issues'] = issues
            context['thumbnails'] = thumbnails
            context['num_of_issue'] = issues.count()
        if self.model == Issue:
            strips_count = Strip.objects.filter(issue=obj).count()
            strips = Strip.objects.filter(issue=obj).order_by('num')[:7]
            context['strips'] = strips
            context['strips_count'] = strips_count
        return context
    
class IndexView(TemplateView):
    template_name = "novels/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        last_issues = Issue.objects.order_by('-pub_datetime')[:14]
        unsort_pubs = Publisher.objects.all()
        sort_pubs = sorted(unsort_pubs, key= lambda t: t.subs.count(), reverse=True)
        top_pubs = sort_pubs[:6]
        
        thumbnails = []
        titles = []
        for issue in last_issues:
            thumbnails.append(Strip.objects.get(issue=issue,num=0))
            if not(issue.tit in titles):
                titles.append(issue.tit)
        
        context['thumbnails'] = thumbnails
        context['last_issues'] = last_issues
        context['top_pubs'] = top_pubs
        context['titles'] = titles
        return context

@login_required
@require_POST    
def subscribe_to(request, mod):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        obj = get_object_or_404(mod, slug=slug)
        
        if obj.subs.filter(id=user.id).exists():
            obj.subs.remove(user)
            message = 'You described from updates'
            subscribe = False
        else:
            obj.subs.add(user)
            message = 'You subscribe to updates'
            subscribe = True
            
    data = json.dumps({'subs_count': obj.get_subs_count(), 'message': message, 'subscribe': subscribe})
    return HttpResponse(data, content_type='application/json')

def download_issue_archive(request, pk):
    issue = get_object_or_404(Issue, id=pk)
    path = issue.archive.path
    name = path.split('/')[-1]

    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(name)
    response['X-Sendfile'] = smart_str(path)
    return response
