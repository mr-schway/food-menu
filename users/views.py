from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ResgisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
  if request.method == "POST":
    form = ResgisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      messages.success(request, f"Welcome {username}, your account has been created")
      return redirect("login")
  else:
    form = ResgisterForm()
  return render(request, "users/register.html", {"form": form})

def logoutView(request):
  logout(request)
  return render(request, "users/logout.html")

@login_required
def profilePage(request):
  return render(request, "users/profile.html")