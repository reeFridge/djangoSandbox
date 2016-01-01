from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import ListView, DetailView
from blog.models import Post, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

class PostListView(ListView):
    model = Post 
    paginate_by=5
    categorised = False
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        categorised = self.categorised
        context['categorised'] = categorised
        if categorised:
            context['cat_id'] = self.kwargs['pk']
        return context
    
    def get_queryset(self):
        if self.categorised:
            self.category = get_object_or_404(Category, id=self.kwargs['pk'])
            qset = Post.objects.filter(cat__id=self.category.id).order_by('-datetime')
        else:
            qset = Post.objects.order_by('-datetime')            
        return qset 

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = super(PostDetailView, self).get_object()
        user = self.request.user
        liked = post.likes.filter(id=user.id).exists()
        context['liked'] = liked
        return context
    
@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            message = 'You disliked this post'
            liked = False
        else:
            post.likes.add(user)
            message = 'You liked this post'
            liked = True
            
    data = json.dumps({'likes_count': post.get_likes_count(), 'message': message, 'liked': liked})
    return HttpResponse(data, content_type='application/json')
    
