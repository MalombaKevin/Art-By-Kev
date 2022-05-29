from unicodedata import category
from django.db import models

# Create your models here

class Category_Photo(models.Model):
    category_name = models.CharField(max_length=20)

class Where_Photo(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    category_photo = models.ForeignKey(Category_Photo, on_delete=models.CASCADE)
    where_photo =models.ForeignKey(Where_Photo,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    def save_image(self):
        self.save()




    
    # image = models.ImageField(upload_to = 'images/')



    




