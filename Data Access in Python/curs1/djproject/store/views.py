import csv
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse, HttpResponse
# Create your views here.

def store_list_view(request):
    print(request.GET.get("search"))
    search = request.GET.get("search")
    if search:
        products = Product.objects.filter(title__contains=search) 
    else:
        products =  Product.objects.all()
    return render(request, 'store_list.html', {'products':products})

def store_details_view(request, slug):
    product_details = get_object_or_404(Product, slug=slug)
    return render(request, 'store_details.html', {'product': product_details})
 
def jsonproducts_view(request):
    products =  list(Product.objects.all())
    products = [ {"nume":product.name, "pret":product.price}   for product in products  ]
    return JsonResponse({"products": products})


def csvproducts_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  'attachment; filename="products.csv"'
    writer = csv.writer(response)
    writer.writerow(('Titlu', 'Slug', 'Pret', 'Description'))
    products =  list(Product.objects.all())
    for prod in products:
        writer.writerow((prod.name, prod.slug, prod.price, prod.description))
    return response
