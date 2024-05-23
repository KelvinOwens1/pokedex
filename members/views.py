from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import CreateUserForm, UpdateProfileForm, PasswordChangingForm


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('profile')


def password_success(request):
    return render(request, 'registration/password_succes.html', {})


class UserRegisterView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user