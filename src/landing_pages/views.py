from django.shortcuts import render
from . forms import LandingPageForm


def home_page(request, *args, **kwargs):
    title = "Welcome Home"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data.get("email"))
        print(form.cleaned_data)
        form=LandingPageForm(None)
    # print("Your email is :", request.POST.get("email"))
    context = { 
        "title": title,
        "form": form
    }
    return render(request, "landing_pages/home.html",context)

