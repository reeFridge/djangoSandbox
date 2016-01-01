from django import template
from blog.models import Category
register = template.Library()

@register.inclusion_tag('customtags/results.html')
def get_list():
    categorys = Category.objects.all()
    return {'categorys': categorys}

