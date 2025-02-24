# from django.http import HttpResponse

from django.shortcuts import render
from .forms import LandingPageForm


def home_page(request, *args, **kwargs):
    title = "Welcome Home"
    form = LandingPageForm()
    context = { 
        "title": title,
        "form": form
    }
    return render(request, "home.html",context)

def rand_page(request, *args, **kwargs):
    title = "Welcome to abc"
    form = LandingPageForm()
    context = { 
        "title": title,
        "form": form
    }
    return render(request, "rand.html",context)
