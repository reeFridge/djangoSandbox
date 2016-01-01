from django.db import models
import datetime
import random
import string
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:Categorise_list', args=[self.id])

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"Publication date")
    content = models.TextField(max_length=10000)
    cat = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)   
    author = models.ForeignKey(User, null=True)
    imgURL = models.CharField(max_length=255, default="http://placehold.it/200x140")
    tags = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(default=slugify(''.join(random.sample(string.ascii_lowercase, 10))))
    likes = models.ManyToManyField(User, related_name = 'likes')

    def __str__(self):
        return self.title
    
    def tags_list(self):
        return self.tags.split(";")

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])
    
    def get_likes_count(self):
        return self.likes.count()
    
    def get_descr_of_post(self):
        descr = self.content[:350] + ' ...'        
        return descr
    
    def save(self, *args, **kwargs):
        if slugify(self.title) != '':
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

