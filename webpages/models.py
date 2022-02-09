from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Newsletter(models.Model):

    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
