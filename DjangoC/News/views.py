from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News, Human

def index(request):
#    print(request)
#    return HttpResponse('<h1>Привет народ!</h1>')
    news=News.objects.all()
    human=Human.objects.all()
    contxt={
        'news': news,
        'title': '-Список новостей-',
        'human': human,
        'htitle': 'Список людей'
    }
    return render(request, 'index.html', context=contxt)

''' res='<h1>Список новостей</h1>'
    for i in news:
        res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p>\n</div>\n<hr>'
    return HttpResponse(res)'''
