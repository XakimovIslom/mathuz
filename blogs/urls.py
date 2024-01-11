from django.urls import path
from .views import post_list, about_me, post_detail


urlpatterns = [
    path('', post_list, name='post-list'),
    path('about/', about_me, name='about-me'),
    path('post/detail/<int:pk>/', post_detail, name='post-detail'),

]
