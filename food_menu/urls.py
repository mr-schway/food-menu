from django.urls import path
from . import views

app_name = "food_menu"
urlpatterns = [
  # /food/
  path("", views.IndexClassView.as_view(), name="index"),
  # /food/1
  path("<int:pk>/", views.FoodDetail.as_view(), name="detail"),
  path("item/", views.item, name="item"),
  # add item
  path("add/", views.CreateItem.as_view(), name="createItem"),
  # edit item
  path("update/<int:itemId>/", views.updateItem, name="updateItem"),
  # delete item
  path("delete/<int:itemId>/", views.deleteItem, name="deleteItem"),
]