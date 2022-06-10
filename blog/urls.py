'''
Blog urls
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("<uuid>/", views.PostDetail.as_view(), name='post_detail'),
]
