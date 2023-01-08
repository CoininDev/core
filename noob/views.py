from django.shortcuts import render

def index(request):
    return render(request, 'index')

def contato(request):
    return render(request, 'contato')