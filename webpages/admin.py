from django.contrib import admin
from .models import Contact, Newsletter, Dishes
from django.utils.html import format_html

# Register your models here.


class ContactDisplay(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "created_date")
    list_display_links = ("id", "name", "email")


class NewsletterDisplay(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_date")
    list_display_links = ("id", "name", "email")


class DishesDisplay(admin.ModelAdmin):
    def indexpage(self, object):
        return format_html('<img src="{}" width=50 />'.format(object.photo_dish.url))

    list_display = (
        "id",
        "title",
        "price",
        "created_date",
        "indexpage",
    )
    search_fields = ("title", "price")
    list_display_links = ("id", "title", "indexpage")


admin.site.register(Contact, ContactDisplay)
admin.site.register(Newsletter, NewsletterDisplay)
admin.site.register(Dishes, DishesDisplay)
