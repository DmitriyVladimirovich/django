from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import News, Category

def index(request):
    news = News.objects.all()
    contxt = {
        'news': news,
        'title': '-= Список новостей =-',
    }
    return render(request, 'News/index.html', context=contxt)

def get_category(request, category_id):
    news = News.objects.filter(categ_id=category_id)
    cat = Category.objects.get(pk=category_id)
    contxt = {
        'news': news,
        'cat': cat,
    }
    return render(request, 'News/category.html', context=contxt)







''' res='<h1>Список новостей</h1>'
    for i in news:
        res += f'<div>\n<p>{i.title}</p>\n<p>{i.content}</p>\n</div>\n<hr>'
    return HttpResponse(res)'''