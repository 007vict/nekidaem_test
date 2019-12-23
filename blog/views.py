from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView

from .models import Blog, Subscriber
from .forms import *
from .tasks import post_create


class BlogHomeView(ListView):
    queryset = Blog.objects.all().order_by('-created')
    context_object_name = 'posts'
    template_name = 'blog/post/home.html'


class BlogDetailView(View):
    def get(self, request, pk):
        posts = Blog.objects.get(pk=pk)
        """Automatic request.user mark read post  """
        # if len(posts.read) == 0:
        #     posts.read = []
        #     posts.read.append(request.user.username)
        #     posts.save()
        # if request.user.username not in posts.read:
        #     posts.read.append(request.user.username)
        #     posts.save()
        return render(request, 'blog/post/detail.html', {'posts': posts})


class MyNews(View):
    def get(self, request):
        posts = Blog.objects.filter(author__author__subscriber=request.user) \
            .exclude(read__contains=request.user.username) \
            .order_by('-created')
        formset = ReadNewsFormSet(queryset=posts)
        forms = formset
        form_count = len(forms)
        return render(request, 'blog/post/mynews.html', {'posts': posts,
                                                         'forms': forms,
                                                         'form_count': form_count
                                                         })

    def post(self, request):
        posts = Blog.objects.filter(author__author__subscriber=request.user) \
            .exclude(read__contains=request.user.username) \
            .order_by('-created')
        if request.method == 'POST':
            formset = ReadNewsFormSet(request.POST, queryset=posts)
            if formset.is_valid():
                formset.save()
                for post in posts:
                    if post.reader_news == True:
                        if not post.read:
                            post.read = []
                            post.read.append(request.user.username)
                            post.reader_news = False
                            post.save()
                        else:
                            post.read.append(request.user.username)
                            post.reader_news = False
                            post.save()
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
        subscriber = Subscriber.objects.get(subscriber_id=user_pk, author_id=author_pk).subscriber.username
        author = Subscriber.objects.get(author_id=author_pk, subscriber_id=user_pk).author.username
        return render(request, 'blog/post/subscriber_to.html', {'subscriber': subscriber, 'author': author})


class DeleteSubscriber(View):
    def get(self, request, user_pk, author_pk):
        subscriber = Subscriber.objects.get(subscriber_id=user_pk, author_id=author_pk).subscriber
        author = Subscriber.objects.get(author_id=author_pk, subscriber_id=user_pk).author
        Subscriber.objects.filter(subscriber_id=user_pk, author_id=author_pk).delete()
        return render(request, 'blog/post/subscriber_del.html', {'subscriber': subscriber, 'author': author})


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'blog/post/new_post.html'
    success_url = 'blog:home'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        post_create.delay(instance.id)
        return redirect('blog:home')








