from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from django.core.files import File
import datetime
import shutil
import rarfile
import os
import glob

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
    
STATUS_CHOICES = []
STATUS_CHOICES.append(('Завершен','Completed'))
STATUS_CHOICES.append(('Незавершен','Ongoing'))

rarfile.UNRAR_TOOL = 'rar'



class Publisher(models.Model):
    pub_title = models.CharField(max_length = 255)
    found = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    twitter = models.URLField(verbose_name = u"Twitter")
    website = models.URLField(verbose_name = u"Website")
    imgUrl = models.URLField(default="http://placehold.it/150x150",verbose_name = u"Image")
    abbrev = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    desc = models.TextField(max_length = 1000)
    slug = models.SlugField(max_length = 255,blank=True)
    subs = models.ManyToManyField(User, related_name = 'Subscribers', blank=True)
    imprint_of = models.ForeignKey('Publisher',null=True, on_delete=models.SET_NULL, blank=True)
    
    def get_subs_count(self):
        return self.subs.count()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.pub_title)
        super(Publisher, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.pub_title
    
    def get_short_desc(self):
        return self.desc[:100]
    
    class Meta:
        ordering = ('found',)

class Group(models.Model):
    title = models.CharField(max_length = 255)
    orig_title = models.CharField(max_length = 255)
    publisher = models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    desc = models.TextField(max_length = 1000)
    date = models.DateField(verbose_name = u"Creation date")
    slug = models.SlugField(max_length = 255,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.orig_title)
        super(Group, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title    
    
class Arc(models.Model):
    arc_title = models.CharField(max_length = 255)
    orig_arc_title = models.CharField(max_length = 255)
    publisher = models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    desc = models.TextField(max_length = 1000)    
    slug = models.SlugField(max_length = 255,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.orig_arc_title)
        super(Arc, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.arc_title
    
class Genre(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
        
class Title(models.Model):
    title = models.CharField(max_length = 255)
    orig_title = models.CharField(max_length = 255)
    publisher = models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    imgUrl = models.URLField(default="http://placehold.it/155x235",verbose_name = u"Image")
    translateURL = models.URLField(default="http://",verbose_name = u"Trans")
    arc = models.ForeignKey(Arc,null=True, on_delete=models.SET_NULL,blank=True)
    author = models.CharField(max_length = 255, blank=True)
    artist = models.CharField(max_length = 255, blank = True)
    genre = models.ManyToManyField(Genre, related_name = 'Genre', blank = True)
    status = models.CharField(max_length = 255,choices = STATUS_CHOICES, default=STATUS_CHOICES[0])
    desc = models.TextField(max_length = 1000)
    date = models.DateField(verbose_name = u"Publication date")
    slug = models.SlugField(max_length = 255,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.orig_title)
        super(Title, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class Character(models.Model):
    name = models.CharField(max_length = 255)
    real_name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    publisher = models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField(Group,related_name = "Groups")
    firstIssue = models.ForeignKey('Issue',null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length = 255,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Issue(models.Model):
    number = models.PositiveIntegerField(null=True)
    trans_name = models.CharField(max_length = 255,blank=True,null=True)
    name = models.CharField(max_length = 255,blank=True,null=True)
    date = models.DateField(verbose_name = u"Publication date")
    publisher = models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    arc = models.ForeignKey(Arc,null=True, on_delete=models.SET_NULL, blank = True)
    archive = models.FileField(blank=True)
    groups = models.ManyToManyField(Group,related_name = "IssueGroups",blank=True)
    characters = models.ManyToManyField(Character,related_name = "Chars",blank=True)
    tit = models.ForeignKey(Title, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length = 255,blank=True)
    pub_datetime = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.tit.slug+'-'+str(self.number))
        for field in self._meta.fields:
            if field.name == 'archive':
                field.upload_to = 'novels/static/novels/comics/%s/%s/%s' % (self.publisher.slug, self.tit.slug, self.number)
        super(Issue, self).save(*args, **kwargs)        
        
    def __str__(self):
        return self.tit.orig_title + "-" + str(self.number)

class Strip(models.Model):
    num = models.PositiveIntegerField(null=True)
    issue = models.ForeignKey(Issue,null=True, on_delete=models.SET_NULL)
    img_file_name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 255,blank=True,primary_key=True)
    
    def save(self, *args, **kwargs):
        s = self.issue.tit.slug+'-'+str(self.issue.number)+'-'+str(self.num)
        self.slug = slugify(s)
        super(Strip, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.issue.tit.slug+'-'+str(self.issue.number)+'-'+str(self.num)
    
    def get_abs_url(self):
        return '/static/novels/comics/' + self.issue.tit.publisher.slug + '/' + self.issue.tit.slug + '/' + str(self.issue.number) + '/img/' + self.img_file_name
    
    
@receiver(pre_delete, sender=Issue)
def Issue_before_delete(sender, instance, **kwargs):
    name = instance.archive.path.split('/')[-1]
    path = instance.archive.path.replace(name,'')
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print('No such directory: '+path)
    instance.archive.delete(False)
    Strip.objects.filter(issue=instance).delete()
    
@receiver(post_save, sender=Issue)
def Issue_after_save(sender, instance, **kwargs):
    arch = rarfile.RarFile(instance.archive.path, 'r')
    name = instance.archive.path.split('/')[-1]
    path = instance.archive.path.replace(name,'')+'img/'
    arch.extractall(path)
    os.chdir(path)
    a = []
    for file in glob.glob("*.jpg"):
        a.append(file)
    a.sort()
    for idx, strip in enumerate(a):
        reopen = open(path+strip, "rb")
        dj_file = File(reopen)
        new_strip = Strip(num=idx, issue=instance, img_file_name=strip)
        new_strip.save()
        
        
        
        
    

    
    
    

    
    
    
    
    
