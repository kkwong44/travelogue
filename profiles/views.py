'''
Views for User Profile App
'''
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Users
from .forms import ProfileForm


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''
    Edit and update user profile
    '''
    model = Users
    form_class = ProfileForm
    template_name = "profiles/update.html"

    def form_valid(self, form):
        '''
        Validate user access rights to edit profile
        '''
        messages.success(
            self.request, 'Your profile has been successfully updated.')
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        Validate user identity to edit own profile
        '''
        user = self.get_object()
        if self.request.user.username == user.username:
            return True
        return False
