from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Human, Profession

def hindex(request):
    human=Human.objects.all()
#    profs = Profession.objects.all()
    contxt={
        'human': human,
#        'profs': profs,
        'title': '-= Список людей =-',
    }
    return render(request, 'hindex.html', context=contxt)

def get_profession(request, profession_id):
    human = Human.objects.filter(profs_id=profession_id)
#    profs = Profession.objects.all()
    prof = Profession.objects.get(pk=profession_id)
    contxt = {
        'human': human,
#        'profs': profs,
        'prof': prof,
    }
    return render(request, 'profession.html', context=contxt)