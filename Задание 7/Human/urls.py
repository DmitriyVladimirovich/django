from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from Human.views import hindex

urlpatterns = [
    path('',hindex),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)