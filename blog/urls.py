from django.urls import path

from blog.views import (
    BlogDetailView,
    BlogDeleteView,
    BlogCreateView,
    BlogListView,
    BlogUpdateView
)

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]