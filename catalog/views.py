from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(
        request,
        'catalog/index.html',
        context={
            'products': Product.objects.all()
        }
    )


def contacts(request):
    return render(request, 'catalog/contacts.html')


def detail_product_view(request, product_pk):
    return render(
        request,
        'catalog/detail_product.html',
        context={
            'product': Product.objects.get(pk=product_pk)
        }
    )
