from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('detail/<int:pk>/<slug:title>/', BlogDetailView.as_view(), name='detail'),
    path('user_info/<int:pk>/<slug:username>/', UserInfo.as_view(), name='user'),
    path('news/', MyNews.as_view(), name='my_news'),
    path('mysubcribers/', MySubscriber.as_view(), name='subcribers'),
    path('<int:user_pk>/subscribe_to/<int:author_pk>/', AddSubscriber.as_view(), name='subscribe_to_authors'),
    path('<int:user_pk>/unsubscribe_to/<int:author_pk>/', DeleteSubscriber.as_view(), name='unsubscribe_to_authors'),
]