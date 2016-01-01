from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from ExtUser.models import UserProfile

from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main Information',     {'fields': ['title','cat']}),
        ('Image URL',                {'fields': ['imgURL']}),
        ('Short Description and Tags',    {'fields': ['descr', 'tags']}),
        ('Full Content',         {'fields': ['content']}),
        ('Date Information',     {'fields': ['datetime'], 'classes': ['collapse']}),
    ]
    list_display = ('title','cat','get_likes_count','datetime')
    list_filter = ['datetime']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
