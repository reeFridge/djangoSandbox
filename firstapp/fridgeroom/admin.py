from django.contrib import admin
from fridgeroom.models import StandartPublication

class PubAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main Information',     {'fields': ['title']}),
        ('Full Content',         {'fields': ['content']}),
        ('Date Information',     {'fields': ['datetime'], 'classes': ['collapse']}),
    ]
    list_display = ('title','datetime')
    list_filter = ['datetime']
    
admin.site.register(StandartPublication, PubAdmin)
    