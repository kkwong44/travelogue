"""
Import libraries for User Profile App
"""
from django.contrib.auth.models import User
from django.urls import reverse


class Users(User):
    '''
    Modify user model
    '''
    class Meta:
        '''
        Inherent from default
        '''
        proxy = True

    def get_absolute_url(self):
        '''
        Redirect to home page
        '''
        return reverse('home')
