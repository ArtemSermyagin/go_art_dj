from django.urls import path

from catalog.views import contacts, detail_product_view, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path('', index),
    path('contacts/', contacts),
    path('products/<int:product_pk>/', detail_product_view)
]
