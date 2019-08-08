from django.urls import path

from blog.views import BlogHomeView, BlogDetailView, MyNews

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:title>/', BlogDetailView.as_view(), name='detail'),
    path('news/', MyNews.as_view(), name='my_news'),
]