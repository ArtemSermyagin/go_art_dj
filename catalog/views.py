from django.views.generic import TemplateView, DetailView

from catalog.models import Product


class ProductListView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'
    template_name = 'catalog/detail_product.html'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'



