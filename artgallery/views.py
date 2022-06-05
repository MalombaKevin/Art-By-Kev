from django.shortcuts import render

from artgallery.models import Image

# Create your views here.
def artgallery(request):
    images = Image.objects.all()
    
    
    return render(request, 'index.html', {"images":images})

def artview(request, id):
    art = Image.objects.filter(id=id)
    
    return render(request, 'artview.html', {"images":art})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message": message, "categories":searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})

def location_search(request):
    if 'location' in request.GET and request.GET['location']:
        search_term = request.GET.get('location')
        search_locations= Image.search_by_location(search_term)
        message = f"{search_term}"
        return render(request, 'locations.html', {"message": message, 'places': search_locations})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'locations.html', {"message":message})