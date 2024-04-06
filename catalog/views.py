from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, \
    CreateView, ListView, DeleteView

from catalog.models import Product, Version

from catalog.forms import ProductForm, VersionForm


class ProductListView(ListView):
    template_name = 'catalog/index.html'
    queryset = Product.objects.filter(versions__is_actual=True)
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'
    template_name = 'catalog/detail_product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    login_url = reverse_lazy("login")
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = self.request.user
            product.save()
            Version.objects.create(
                name="Версия 1",
                number=0,
                is_actual=True,
                product=product
            )
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    login_url = reverse_lazy("login")
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
            for version in Version.objects.filter(
                    product_id=self.kwargs['product_pk'], is_actual=True):
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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    login_url = reverse_lazy("login")
    pk_url_kwarg = 'product_pk'
    success_url = reverse_lazy('home')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
