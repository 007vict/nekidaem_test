from django.contrib import admin
from .models import Blog, Subscriber

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body', 'created', 'read')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('author', 'subscriber')

