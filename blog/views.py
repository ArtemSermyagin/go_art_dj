from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import (
    DetailView,
    DeleteView,
    CreateView,
    ListView,
    UpdateView
)

from blog.models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        instance = super().get_object(queryset)
        instance.number_of_views += 1
        instance.save()
        return instance


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.slug = slugify(blog.title)
            blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview']

    def get_success_url(self):
        return reverse('blog_detail', args=(self.kwargs.get('slug'),))


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
