from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .utilities import *

class BlogModel(models.Model):
    title = models.CharField(max_length = 1000)
    content = FroalaField()
    slug = models.SlugField(max_length = 1000)
    image = models.ImageField(upload_to='blog')
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): #Save Override method
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)