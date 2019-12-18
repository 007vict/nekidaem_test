from __future__ import absolute_import, unicode_literals

from urllib import request

from celery import task, shared_task
from django.core.mail import send_mail

from .models import Blog

@shared_task
def post_create(id):
    posts = Blog.objects.get(id=id)
    if posts.author.followers.all:
        for user in posts.author.followers.all():
            subject = 'New post "{}"'.format(posts.title)
            message = 'Dear {},\n\nYou have successfully a new post "{}" - http://{}:1337{} for author {}.'.format(user.username, posts.title, request.localhost(), posts.get_absolute_url(), posts.author)
            send_mail(subject, message, 'super_vg@bk.ru', [user.email])