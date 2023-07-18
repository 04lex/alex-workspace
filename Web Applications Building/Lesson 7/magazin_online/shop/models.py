from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=200)