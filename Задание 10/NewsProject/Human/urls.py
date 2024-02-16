from django.contrib import admin
from django.urls import path

from Human.views import hindex, get_profession

urlpatterns = [
    path('',hindex, name='HomeH'),
    path('prof/<int:profession_id>',get_profession, name='Profession')
]
