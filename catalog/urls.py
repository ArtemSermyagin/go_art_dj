from django.urls import path

from catalog.views import ContactView, ProductDetailView, ProductListView, create_product_view, ProductUpdateView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path('contacts/', ContactView.as_view()),
    path('products/<int:product_pk>/', ProductDetailView.as_view()),
    path('catalog/create_product/', create_product_view, name='create_product'),
    path('products/<int:product_pk>/update/', ProductUpdateView.as_view(), name='update_product'),

]
