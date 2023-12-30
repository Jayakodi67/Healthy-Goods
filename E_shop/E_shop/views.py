from django.shortcuts import render,redirect
from store_app.models import Product,Categories,Filter_price

def BASE(request):
    return render(request,'Main/base.html')


def HOME(request):
    product = Product.objects.filter(status = 'Publish')
    context = {
        'product': product,
    }
    return render(request,'Main/index.html',context)

def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    categories = Categories.objects.all()
    filter_price = Filter_price.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories = CATID)
    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories':categories,
        'filter_price':filter_price,
    }
    return render(request,'Main/product.html',context)


def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product': product
    }
    return render(request, 'Main/search.html',context)


def PRODUCT_DETAIL_PAGE(request,id):
    prod = Product.objects.filter(id = id).first()
    context = {
        'prod': prod
    }
    return render (request,'Main/product_single.html',context)