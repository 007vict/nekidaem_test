from django.contrib import admin
from .models import Blog, Subscriber

from .tasks import post_create


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'body', 'created', 'read')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            post_create.delay(obj.id)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('author', 'subscriber',)





