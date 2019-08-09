from django.contrib.auth.models import User
from django.views.generic import View, ListView, DetailView, TemplateView

from .models import Blog, Subscriber

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

class UserInfo(DetailView):
    model = User
    template_name = 'blog/post/user_info.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'author'


class MuSubscriber(ListView):
    model = Subscriber
    context_object_name = 'author'
    template_name = 'blog/post/mysubcribers.html'



















