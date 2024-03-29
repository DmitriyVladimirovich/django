from django.contrib import admin

# Register your models here.
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','categ','title','content','created_at','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_filter = ('is_published', 'categ')
    list_editable = ['categ','is_published']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)