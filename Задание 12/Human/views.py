from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import HumanForm
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

def view_human(request, human_id):
    human_item=get_object_or_404(Human, pk=human_id)
    contxt={
        'human_item': human_item,
    }
    return render(request, 'view_human.html',context=contxt)

def add_human(request):
    if request.method=='POST':
        form=HumanForm(request.POST)
        if form.is_valid():
            human=form.save()
            return redirect(human)
    else:
        form=HumanForm()
    return render(request, 'add_human.html', {'form':form})