from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import datetime
import random
import string

class Publication(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"Publication date")
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if slugify(self.title) != '':
            self.slug = slugify(self.title)
        super(Publication, self).save(*args, **kwargs)
        
class StandartPublication(Publication):
    content = models.TextField(max_length=1000) 
    
    def get_short_content(self):
        descr = self.content[:350] + ' ...'        
        return descr
