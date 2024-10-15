from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    
@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=username)

    else:

        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})

def profile_view(request, username):
    user =get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    context = {
        'user': user,
        'profile': profile,
    }
    return render (request, 'profile.html', context)
            