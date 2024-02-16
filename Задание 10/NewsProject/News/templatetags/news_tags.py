from News.models import Category
from django import template

register=template.Library()
@register.simple_tag(name='get_list_categories')

def get_categories():
    return Category.objects.all()

@register.inclusion_tag('News/list_categories.html')

def show_categories(arg1='Category', arg2='list'):
    cats=Category.objects.all()
    return {'cats': cats, 'arg1':arg1, 'arg2': arg2}