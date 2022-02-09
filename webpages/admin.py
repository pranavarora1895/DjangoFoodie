from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.


class ContactDisplay(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "created_date")
    list_display_links = ("id", "name", "email")


class NewsletterDisplay(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_date")
    list_display_links = ("id", "name", "email")


admin.site.register(Contact, ContactDisplay)
admin.site.register(Newsletter, NewsletterDisplay)
