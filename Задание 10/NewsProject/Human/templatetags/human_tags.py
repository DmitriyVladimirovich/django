from Human.models import Profession
from django import template

register=template.Library()
@register.simple_tag(name='get_list_professions')

def get_professions():
    return Profession.objects.all()

@register.inclusion_tag('list_professions.html')

def show_professions(arg1='Profession', arg2='list'):
    profs=Profession.objects.all()
    return {'profs': profs, 'arg1':arg1, 'arg2': arg2}