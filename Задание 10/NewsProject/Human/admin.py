from django.contrib import admin

# Register your models here.
from .models import Human, Profession

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id','profs','fname','lname','hage','passp')
    list_display_links = ('id','fname')
    search_fields = ('fname','lname')
    list_editable = ('profs','hage')

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)
