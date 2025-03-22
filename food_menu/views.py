from django.shortcuts import redirect, render
from django.http import HttpResponse
from food_menu.item_form import ItemForm
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

def createItem(request):
  form = ItemForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('food_menu:index')
  
  return render(request, "food_menu/item_form.html", {"form": form})

def updateItem(request, itemId):
  item = Item.objects.get(id=itemId)
  form = ItemForm(request.POST or None, instance=item)

  if form.is_valid():
    form.save()
    return redirect('food_menu:index')
  
  return render(request, "food_menu/item_form.html", {"form": form, "item": item})

def deleteItem(request, itemId):
  item = Item.objects.get(id=itemId)

  if request.method == "POST":
    item.delete()
    return redirect('food_menu:index')
  
  return render(request, "food_menu/item_delete.html", {"item": item})