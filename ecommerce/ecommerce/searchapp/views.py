from django.http import request
from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q


# Create your views here.


def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        p = Product.objects.all().filter(Q(slug__contains=query) )
        return render(request, "search.html", {'query': query, 'products': p})
