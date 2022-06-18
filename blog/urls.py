'''
Blog urls
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('country/', views.PopularList.as_view(), name='country_list'),
    path("<uuid>/", views.PostDetail.as_view(), name='post_detail'),
    path("like/<uuid>", views.PostLike.as_view(), name='post_like'),
    path("post/newpost/", views.PostCreate.as_view(), name='post_create'),
    path("<pk>/updatepost/", views.PostUpdate.as_view(), name='post_update'),
    path("<pk>/deletepost/", views.PostDelete.as_view(), name='post_delete'),
]
