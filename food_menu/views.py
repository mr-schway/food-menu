from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
  itemList = Item.objects.all()
  return HttpResponse(itemList)

def cool(request):
  return HttpResponse("Cool!!!!!!!!!")

def item(request):
  return HttpResponse("This is an item view")