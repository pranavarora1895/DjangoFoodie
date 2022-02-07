from urllib import request
from django.shortcuts import render

# Create your views here.


def index(request):

    data = {"index_page": "active"}
    return render(request, "index.html", data)


def about(request):
    data = {"about_page": "active"}
    return render(request, "about.html", data)


def recipe(request):
    data = {"recipe_page": "active"}
    return render(request, "recipe.html", data)


def contact(request):
    data = {"contact_page": "active"}
    return render(request, "contact.html", data)
