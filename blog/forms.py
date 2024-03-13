from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'location', 'body')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'add-post' }),
           'location': forms.TextInput(attrs={'class': 'add-post', 'placeholder': 'eg. Newquay, Cornwall'}),
           'body': forms.Textarea(attrs={'class': 'add-post' }),
        }

