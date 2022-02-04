from urllib import request
from django.shortcuts import render

# Create your views here.


def index(request):
    marks = [67, 34, 89, 90, 23, 11, 89, 45, 23, 12, 6, 8, 9, 0]

    data = {
        "firstname": "Sahana",
        "lastname": "Parihar",
        "class": 6,
        "is_pass": True,
        "marks": marks,
    }
    return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def recipe(request):
    return render(request, "recipe.html")


def contact(request):
    return render(request, "contact.html")
