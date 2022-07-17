"""
Import libraries
"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


STATUS = ((0, "Draft"), (1, "Published"), (2, "Disapproved"))


class Post(models.Model):
    '''
    Inherit standard model to make Post model
    '''
    title = models.CharField(max_length=45, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    country = CountryField(blank_label='(select country)')
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        '''
        Sort post by creation date in descending order
        '''
        ordering = ["-created_on"]

    def __str__(self):
        '''
        Magic method that returns s string expression
        '''
        return self.title

    def number_of_likes(self):
        '''
        Method to returns number of likes
        '''
        return self.likes.count()

    def get_absolute_url(self):
        '''
        Redirect to detail post
        '''
        return reverse('post_detail', kwargs={'uuid': self.pk})


class Comment(models.Model):
    '''
    Inherit standard model to make Comment model
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        Sort post by creation date in ascending order
        '''
        ordering = ["created_on"]

    def __str__(self):
        '''
        Magic method that returns s string expression
        '''
        return f"Comment {self.body} by {self.name}"
