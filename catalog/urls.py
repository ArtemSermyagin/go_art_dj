from django.urls import path

from catalog.views import ContactView, ProductDetailView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path('contacts/', ContactView.as_view()),
    path('products/<int:product_pk>/', ProductDetailView.as_view()),
]
