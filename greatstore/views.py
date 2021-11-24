from django.shortcuts import render
from store.models import Offers
from store.models import Trending, ReviewRating, New, Product


def home(request):
    products = Trending.objects.all().filter(is_available=True).order_by('-modified_date')
    offers   = Offers.objects.all().filter(is_available=True)
    new = New.objects.all().filter(is_available=True).order_by('-created_date')
    all_products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    deals = Product.objects.all().filter(is_available=True).order_by('-created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'reviews'  : reviews,
        'products' : products,
        'offers'   : offers,
        'new'      : new,
        'all_products' : all_products,
        'deals' : deals,
    }

    return render(request, 'home.html',context)

def faq(request):
    return render(request, 'faq.html')
