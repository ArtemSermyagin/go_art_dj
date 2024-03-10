from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.models import Product


class HomePageView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:5]
        return context

# def index(request):
#     return render(
#         request,
#         'catalog/index.html',
#         context={
#             'products': Product.objects.all()
#         }
#     )


def contacts(request):
    return render(request, 'catalog/contacts.html')

    # def get_contacts_data(self, **kwargs):
    #     context = super().get_contacts_data(**kwargs)
    #     context['products'] = Product.objects.all()[:5]
    #     return context

def detail_product_view(request, product_pk):
    return render(
        request,
        'catalog/detail_product.html',
        context={
            'product': Product.objects.get(pk=product_pk)
        }
    )
