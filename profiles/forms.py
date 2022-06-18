'''
Forms
'''
from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    '''
    User profile form
    '''
    class Meta:
        '''
        Fields from user model
        '''
        model = User
        fields = ('first_name', 'last_name', 'email', )
