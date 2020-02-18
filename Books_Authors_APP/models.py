from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 20)

class Author(models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 25)
    books = models.ManyToManyField(Book, related_name = "authors")