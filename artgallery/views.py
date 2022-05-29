from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def artgallery(request):
    return render(request, 'artgallery.html')
