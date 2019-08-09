from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author',)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} follow {}'.format(self.subscriber, self.author)

User.add_to_class('following',
                  models.ManyToManyField(User,
                                         through=Subscriber,
                                         related_name='followers',
                                         symmetrical=False))

