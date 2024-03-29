from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, CreateView, ListView, DeleteView

from catalog import forms
from catalog.models import Product, Category, Version

from django.shortcuts import render, redirect
from catalog.forms import ProductForm, VersionForm


class ProductListView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(versions__is_actual=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'
    template_name = 'catalog/detail_product.html'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


# class ProductListView(ListView):
#     model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog/index.html')


class ProductUpdateView(UpdateView):
    model = Product
    pk_url_kwarg = 'product_pk'
    template_name = 'catalog/product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        return context

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            for version in Version.objects.filter(product_id=self.kwargs['product_pk'], is_actual=True):
                version.is_actual = False
                version.save()

            Version.objects.create(
                name=self.request.POST['name_version'],
                number=self.request.POST['number'],
                is_actual=True,
                product=product
            )
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            Version.objects.create(
                name="Версия 1",
                number=0,
                is_actual=True,
                product=product
            )
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

# def create_product_view(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             name = request.POST.get('name')
#             description = request.POST.get('description')
#             price = request.POST.get('price')
#             image = request.POST.get('image')
#             category = Category.objects.get(id=request.POST.get('category'))
#             try:
#                 Product.objects.create(name=name, description=description, price=price, image=image, category=category)
#             except IntegrityError:
#                 pass
#         return redirect('home')
#     form = ProductForm()
#     return render(request, 'catalog/product_create.html', {'form': form})
