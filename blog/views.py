'''
Django Views
'''
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    '''
    Create view for the list of posts
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 4


class PostDetail(View):
    '''
    Create view for individual post
    '''
    def get(self, request, uuid, *args, **kwargs):
        '''
        Use uuid to get post
        '''
        queryset = Post.objects.filter(status=1, id=uuid)
        post = get_object_or_404(queryset)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
