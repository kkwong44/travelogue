'''
Forms
'''
from django import forms
from .models import Comment, Post


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
        labels = {'body': 'Comment:'}


class CreatePostForm(forms.ModelForm):
    '''
    Create new post
    '''

    class Meta:
        '''
        Form details
        '''
        model = Post
        fields = ('title', 'country', 'excerpt', 'featured_image', 'content', )
        labels = {'excerpt': 'Short Description'}
