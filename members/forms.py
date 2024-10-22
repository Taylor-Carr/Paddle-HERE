from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    delete_profile_image = forms.BooleanField(required=False, label='Delete Profile Picture', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    delete_banner_image = forms.BooleanField(required=False, label='Delete Profile Banner', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = UserProfile
        fields = ['proficiency', 'bio', 'profile_image', 'delete_profile_image','banner_image', 'delete_banner_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your paddling journey:', 'rows': 4}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'banner_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'proficiency': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'profile_image': 'Upload Profile Picture',
            'banner_image': 'Upload Profile Banner',
            'bio': 'Update your bio:',
        }