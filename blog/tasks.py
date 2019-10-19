from celery import task
from django.core.mail import send_mail
from .models import Blog

@task
def post_create(instance_id):
    posts = Blog.objects.get(id=instance_id)
    for user in posts.author.followers.all():
        subject = 'New post "{}"'.format(posts.title)
        message = 'Dear {},\n\nYou have successfully a new post "{}" for author {}.'.format(user.username, posts.title, posts.author)
        send_mail(subject, message, 'super_vg@bk.ru', [user.email])