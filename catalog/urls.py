from django.urls import path

from catalog.views import (
    ContactView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    ProductCreateView, ProductDeleteView
)

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path('contacts/', ContactView.as_view()),
    path(
        'products/<int:product_pk>/',
        ProductDetailView.as_view(),
        name='detail_product'
    ),
    path(
        'catalog/create_product/',
        ProductCreateView.as_view(),
        name='create_product'
    ),
    path(
        'products/<int:product_pk>/update/',
        ProductUpdateView.as_view(),
        name='update_product'
    ),
    path(
        'products/<int:product_pk>/delete/',
        ProductDeleteView.as_view(),
        name='delete_product'
    ),
]
