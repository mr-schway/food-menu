from django.shortcuts import redirect, render
from django.http import HttpResponse
from food_menu.item_form import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
# def index(request):
#   itemList = Item.objects.all()
#   context = {
#     "itemList": itemList,
#   }
#   return render(request, "food_menu/index.html", context)

class IndexClassView(ListView):
  model = Item
  template_name = "food_menu/index.html"
  context_object_name = "itemList"

# def detail(request, itemId):
#   item = Item.objects.get(pk=itemId)
#   context = {
#     "item": item,
#   }
#   return render(request, "food_menu/detail.html", context)

class FoodDetail(DetailView):
  model = Item
  template_name = "food_menu/detail.html"

def item(request):
  return HttpResponse("This is an item view")

# def createItem(request):
#   form = ItemForm(request.POST or None)

#   if form.is_valid():
#     form.save()
#     return redirect('food_menu:index')
  
#   return render(request, "food_menu/item_form.html", {"form": form})

class CreateItem(CreateView):
  model = Item
  fields = ["item_name", "item_desc", "item_price", "item_image"]
  template_name = "food_menu/item_form.html"
  def form_valid(self, form):
    form.instance.user_name = self.request.user
    return super().form_valid(form)
  


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