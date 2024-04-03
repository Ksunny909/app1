from multiprocessing import context
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
  context ={
    'title': 'Home',
    'content': 'Главная страница машазина'
	}
  return render(request,'main/index.html', context)


def about(request):
    return HttpResponse('about page')
