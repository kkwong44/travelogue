'''
Administration to Django Control Panel
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Register Blog Posts
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    Manage Post Model and use django summernote for the content
    '''
    list_display = ('title', 'country', 'status', 'created_on')
    search_fields = ['title', 'country', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    actions = ['publish_posts', 'disapprove_posts']

    def publish_posts(self, request, queryset):
        '''
        Bulk action to publish posts
        '''
        queryset.update(status=1)

    def disapprove_posts(self, request, queryset):
        '''
        Bulk action to disapprove posts
        '''
        queryset.update(status=2)


# Register Post Comments
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Manage Comment Model
    '''
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        '''
        Bulk action to approve comments
        '''
        queryset.update(approved=True)

    def disapprove_comments(self, request, queryset):
        '''
        Bulk action to disapprove comments
        '''
        queryset.update(approved=False)
