from django.shortcuts import render
from .models import Cloth

def index(request):
    if 'brand' in request.GET:
        c = request.GET['brand']
        y = request.GET['size']
        n = request.GET['price']
        t = request.GET['color']
        Cloth.objects.create(brand=c,size=y,price=n,color=t)

    clothes = Cloth.objects.all()
    
    return render(request, 'index.html', {'clothes': clothes})
