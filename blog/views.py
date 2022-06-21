'''
Django Views
'''
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Post
from .forms import CommentForm, CreatePostForm


class PostList(generic.ListView):
    '''
    Create view for the list of posts
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
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
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, uuid, *args, **kwargs):
        '''
        Post comment
        '''
        queryset = Post.objects.filter(status=1, id=uuid)
        post = get_object_or_404(queryset)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        messages.success(request, 'Your comment has been submitted.')

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            if request.user.is_superuser:
                comment.approved = True
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    '''
    Post likes
    '''
    def post(self, request, uuid):
        '''
        Like and unlike post
        '''
        post = get_object_or_404(Post, id=uuid)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[uuid]))


class PostCreate(LoginRequiredMixin, generic.CreateView):
    '''
    Create a new post
    '''
    model = Post
    form_class = CreatePostForm
    template_name = "blog/post_create_or_update.html"

    def form_valid(self, form):
        '''
        Validate user access rights to create post
        '''
        messages.success(
            self.request, 'Your post has been successfully added.')
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''
    Edit and update post
    '''
    model = Post
    form_class = CreatePostForm
    template_name = "blog/post_create_or_update.html"

    def form_valid(self, form):
        '''
        Validate user access rights to create post
        '''
        messages.success(
            self.request, 'Your post has been successfully updated.')
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        Validate post author
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Delete Post
    '''
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Your post has been deleted sucessfully!')
        return response

    def test_func(self):
        '''
        Validate post author
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PopularList(generic.ListView):
    '''
    Filter and show list of posts from selected popular country
    '''
    model = Post
    template_name = "blog/post_popular.html"
    paginate_by = 4

    def get_queryset(self):
        '''
        Get posts from selected country
        '''
        queryset = Post.objects.all()
        country = self.request.GET.get('country', None)

        if country:
            queryset = queryset.filter(country=country)

        return queryset


class AuthorPosts(generic.ListView):
    '''
    Filter posts by author
    '''
    model = Post
    template_name = "blog/post_author.html"
    paginate_by = 4

    def get_queryset(self):
        '''
        Get author posts
        '''
        queryset = Post.objects.all()
        author = self.request.GET.get('author', None)
        if author:
            queryset = queryset.filter(author=author)
        return queryset
