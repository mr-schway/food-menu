from django.urls import path
from . import views

app_name = "food_menu"
urlpatterns = [
  # /food/
  path("", views.index, name="index"),
  # /food/1
  path("<int:itemId>/", views.detail, name="detail"),
  path("item/", views.item, name="item"),
  # add item
  path("add/", views.createItem, name="createItem"),
  # edit item
  path("update/<int:itemId>/", views.updateItem, name="updateItem"),
  # delete item
  path("delete/<int:itemId>/", views.deleteItem, name="deleteItem"),
]