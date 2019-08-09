from django.urls import path

from blog.views import BlogHomeView, BlogDetailView, MyNews, MuSubscriber, UserInfo

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:title>/', BlogDetailView.as_view(), name='detail'),
    path('user_info/<int:pk>/', UserInfo.as_view(), name='user'),
    path('news/', MyNews.as_view(), name='my_news'),
    path('mysubcribers/', MuSubscriber.as_view(), name='subcribers'),
]