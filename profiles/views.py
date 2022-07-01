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
        return self.request.user.username == self.get_object().username


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Delete User Account
    '''
    model = Users
    template_name = "profiles/user_confirm_delete.html"
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        '''
        Overwrite message method
        '''
        response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Your account has been deleted sucessfully!')
        return response

    def test_func(self):
        '''
        Validate user
        '''
        return self.request.user.username == self.get_object().username
