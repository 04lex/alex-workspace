from django.db import models
from django.shortcuts import reverse
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published') )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.title

    # @property
    def generate_slug(self):
        return reverse('blog:blog_details_view', args=[self.slug])