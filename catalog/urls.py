from django.urls import path

from catalog.views import index, contacts, detail_product_view

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('products/<int:product_pk>/', detail_product_view)
]

