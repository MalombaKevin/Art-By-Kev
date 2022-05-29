from django.test import TestCase
from .models import Category_Photo, Where_Photo, Image

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.barcelona= Image(image_name = 'Lionel Messi Returns', image_description = 'The best player in the world', category_photo = Category_Photo(category_name = 'football'), where_photo = Where_Photo(country = 'Spain', city = 'Barcelona'))
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.barcelona, Image))

