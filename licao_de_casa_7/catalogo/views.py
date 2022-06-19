import django
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<p1>Página Inicial</p1>')
