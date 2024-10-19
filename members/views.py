from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from blog.models import Post
from django.contrib import messages


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    
@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.userprofile
    posts = Post.objects.filter(author=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=username)

    else:

        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})

@login_required 
def delete_profile(request, username):
    user = get_object_or_404(User, username = username)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        user_profile.delete()
        user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('home')
    return render(request, 'delete_profile.html', {'user': user})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    posts = Post.objects.filter(author=user)
    context = {
        'user': user,
        'profile': profile,
        'posts': posts,
    }
    return render (request, 'profile.html', context)
            