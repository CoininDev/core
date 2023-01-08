from django.contrib import admin
from django.urls import path

from noob.views import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato)
]
