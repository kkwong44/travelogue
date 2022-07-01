'''
URLS for User Profile App
'''
from django.urls import path
from . import views

urlpatterns = [
    path('<pk>/update/',
         views.EditProfile.as_view(), name='edit_profile'),
    path('<pk>/delete/',
         views.DeleteUser.as_view(), name='delete_profile'),
]
