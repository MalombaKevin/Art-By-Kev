from unicodedata import category
from django.db import models

# Create your models here
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    

    
    # image = models.ImageField(upload_to = 'images/')


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
class Where_Photo(models.Model):
    country = models.CharField(max_length=30)



