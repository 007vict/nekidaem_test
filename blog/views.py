from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect
from django.views.generic import View, ListView, DetailView

from .models import Blog, Subscriber
from .forms import *


class BlogHomeView(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'blog/post/home.html'


class BlogDetailView(View):
    def get(self, request, pk, title):
        posts = Blog.objects.get(pk=pk, title=title)
        print(type(posts.read))
        if len(posts.read) == 0:
            posts.read = []
            posts.read.append(request.user.username)
            posts.save()
        if request.user.username not in posts.read:
            posts.read.append(request.user.username)
            posts.save()
        return render(request, 'blog/post/detail.html', {'posts': posts})


class MyNews(View):

    def get(self, request):
        posts = Blog.objects.filter(author__author__subscriber=request.user)\
            .exclude(reader_news=True) \
            .order_by('-created')

        formset = ReadNewsFormSet(queryset=posts)
        forms = formset
        if len(forms) > 0:
            form_count = len(forms)
            return render(request, 'blog/post/mynews.html', {'posts': posts,
                                                             'forms': forms,
                                                             'form_count': form_count
                                                             })
        else:
            return render(request, 'blog/post/mynews.html', {'posts': posts,
                                                             'forms': forms,
                                                             })


    def post(self, request):
        posts = Blog.objects.filter(author__author__subscriber=request.user) \
            .exclude(reader_news=True) \
            .order_by('-created')

        if request.method == 'POST':
            formset = ReadNewsFormSet(request.POST, queryset=posts)
            if formset.is_valid():
                formset.save()
                return redirect('blog:my_news')



class UserInfo(DetailView):
    model = User
    template_name = 'blog/post/user_info.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'author'
    context_object_name = 'author'


class MySubscriber(ListView):
    model = Subscriber
    context_object_name = 'author'
    template_name = 'blog/post/mysubcribers.html'


class AddSubscriber(View):
    def get(self, request, user_pk, author_pk):
        Subscriber.objects.get_or_create(subscriber_id=user_pk, author_id=author_pk)
        subscriber = Subscriber.objects.get(subscriber_id=user_pk)
        author = Subscriber.objects.get(author_id=author_pk)
        return render(request, 'blog/post/subscriber_to.html', {'subscriber': subscriber, 'author': author})


class DeleteSubscriber(View):
    def get(self, request, user_pk, author_pk):
        subscriber = Subscriber.objects.get(subscriber_id=user_pk)
        author = Subscriber.objects.get(author_id=author_pk)
        Subscriber.objects.filter(subscriber_id=user_pk, author_id=author_pk).delete()
        return render(request, 'blog/post/subscriber_del.html', {'subscriber': subscriber, 'author': author})
