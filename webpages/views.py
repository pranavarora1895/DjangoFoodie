from urllib import request
from django.shortcuts import render
from .models import Contact

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
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    data = {"contact_page": "active"}
    return render(request, "contact.html", data)
