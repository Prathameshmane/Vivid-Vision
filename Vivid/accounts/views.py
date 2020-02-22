from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.views.generic import CreateView
from .forms import EditProfileForm

from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("You Have Edited Your Profile...."))
            return redirect('accounts:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)
