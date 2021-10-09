from django.shortcuts import render
from store.models import Trending
from store.models import Offers

def home(request):
    products = Trending.objects.all().filter(is_available=True)
    offers   = Offers.objects.all().filter(is_available=True)
    context = {
        'products' : products,
        'offers'   : offers,
    }

    return render(request, 'home.html',context)
