import email
from urllib import request
from django.shortcuts import render
from .models import Contact, Newsletter, Dishes
from django.db.models import Q

# Create your views here.


def index(request):

    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]

        newsletter = Newsletter(email=email, name=name)
        newsletter.save()

    dishes = Dishes.objects.order_by("-created_date")

    data = {"index_page": "active", "dishes": dishes}
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


def search(request):
    dishes = Dishes.objects.order_by("-created_date")

    if "query" in request.GET:
        query = request.GET["query"]
        if query:
            dishes = dishes.filter(
                Q(title__icontains=query) | Q(price__icontains=query)
            )

    data = {"index_page": "active", "dishes": dishes}
    return render(request, "search.html", data)
