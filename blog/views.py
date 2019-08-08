from django.views.generic import ListView, DetailView

from .models import Blog

class BlogHomeView(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'blog/post/home.html'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'blog/post/detail.html'


class MyNews(ListView):
    template_name = 'blog/post/mynews.html'
    context_object_name = 'posts'
    ordering = ['-created']

    def get_queryset(self):
        return Blog.objects.exclude(author=self.request.user)



















