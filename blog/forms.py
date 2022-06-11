'''
Forms
'''
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    Form for user to leave comments to the post
    '''
    class Meta:
        '''
        Comment only
        '''
        model = Comment
        fields = ('body',)
