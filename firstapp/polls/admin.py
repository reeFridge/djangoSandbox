from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class questionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Content',		{'fields': ['pub_date']}),
		('Date Information',	{'fields': ['question_text'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text','pub_date','was_pub_rcntly')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, questionAdmin)

