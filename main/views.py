from multiprocessing import context
from typing import Any
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories



def index(request) -> HttpResponse:
  context ={
    'title': 'Home - Главная',
    'content': 'Магазин карточек Винкс',
	}
  return render(request,'main/index.html', context)


def about(request):
    return HttpResponse('about page')
