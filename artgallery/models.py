from unicodedata import category
from django.db import models

# Create your models here

class Category_Photo(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

class Where_Photo(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.country
    
    def save_where_photo(self):
        self.save()
    
      
    def update_where_photo(self):
        self.save()
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = models.ImageField(upload_to = 'artphotos/', null=True)
    image_category = models.ForeignKey(Category_Photo, on_delete=models.CASCADE)
    location_taken =models.ForeignKey(Where_Photo,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    
    def update_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__category_name__icontains=search_term)
        return images




    
   



    




