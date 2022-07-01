"""
Import libraries for User Profile App
"""
from django.contrib.auth.models import User
from django.urls import reverse


class Users(User):
    '''
    Use a Proxy Model to extend the existing User model
    '''
    class Meta:
        '''
        Set Proxy Model
        '''
        proxy = True

    def get_absolute_url(self):
        '''
        Redirect to home page
        '''
        return reverse('home')
