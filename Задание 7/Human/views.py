from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Human, Profession

def hindex(request):
    human=Human.objects.all()
#    prof=Profession.objects.all()
    contxt={
        'human': human,
#        'profs': prof,
        'title': '-= Список людей =-',
    }
    return render(request, 'hindex.html', context=contxt)
