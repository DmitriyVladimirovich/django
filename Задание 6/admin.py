from django.contrib import admin

# Register your models here.
from .models import News, Human

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','hage')
    list_display_links = ('id','fname')
    search_fields = ('fname','lname')

admin.site.register(News, NewsAdmin)
admin.site.register(Human, HumanAdmin)