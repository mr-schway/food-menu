from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
  itemList = Item.objects.all()
  context = {
    "itemList": itemList,
  }
  return render(request, "food_menu/index.html", context)

def detail(request, itemId):
  item = Item.objects.get(pk=itemId)
  context = {
    "item": item,
  }
  return render(request, "food_menu/detail.html", context)

def item(request):
  return HttpResponse("This is an item view")