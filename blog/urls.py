from django.urls import path, include

from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:title>/', BlogDetailView.as_view(), name='detail'),
]