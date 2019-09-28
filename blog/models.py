from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    read = JSONField(default=list, blank=True)
    reader_news = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:detail', args=[self.pk,
    #                                         self.title])


class Subscriber(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriber')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author',)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.subscriber)

User.add_to_class('following',
                  models.ManyToManyField(User,
                                         through=Subscriber,
                                         related_name='followers',
                                         symmetrical=False))




