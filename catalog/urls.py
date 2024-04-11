from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ContactView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    ProductCreateView, ProductDeleteView, ProductUnpublishView, ProductUpdateDescriptionView, ProductUpdateCategoryView
)

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path('contacts/', ContactView.as_view()),
    path(
        'products/<int:product_pk>/',
        cache_page(60)(ProductDetailView.as_view()),
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
    path(
        'products/<int:product_pk>/unpublish/',
        ProductUnpublishView.as_view(),
        name='product_unpublish'
    ),
    path(
        'products/<int:product_pk>/update/description/',
        ProductUpdateDescriptionView.as_view(),
        name='product_change_description'
    ),
    path(
        'products/<int:product_pk>/update/category/',
        ProductUpdateCategoryView.as_view(),
        name='product_change_category'
    )
]
