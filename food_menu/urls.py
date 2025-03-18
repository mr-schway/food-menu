from django.urls import path
from . import views

app_name = "food_menu"
urlpatterns = [
  # /food/
  path("", views.index, name="index"),
  # /food/1
  path("<int:itemId>/", views.detail, name="detail"),
  path("item/", views.item, name="item"),
]