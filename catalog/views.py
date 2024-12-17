from django.http import JsonResponse
from .models import Product
from django.db.models import Q, Count
from django.shortcuts import render

# API to list all products
def product_list(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)


# API for category distribution
def category_distribution(request):
    data = Product.objects.values('category').annotate(count=Count('category'))
    return JsonResponse(list(data), safe=False)

def product_table_template(request):
    """
    Renders a template displaying products in a table format.
    """
    products = Product.objects.all()  # Fetch all product data
    return render(request, 'catalog/product_table.html', {'products': products})
