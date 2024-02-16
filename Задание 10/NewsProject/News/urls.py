from django.contrib import admin

from django.urls import path
from News.views import index, get_category

urlpatterns = [
    path('',index, name='Home'),
    path('cat/<int:category_id>',get_category, name='Category')
]

