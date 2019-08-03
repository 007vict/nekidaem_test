from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Blog

class BlogListView(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'posts'
    # paginate_by = 10
    template_name = 'blog/post/home.html'

class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    context_object_name = 'post'
    template_name = 'blog/post/detail.html'



