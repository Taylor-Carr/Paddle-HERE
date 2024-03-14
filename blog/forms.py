from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'location','author', 'body')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'add-post' }),
           'location': forms.TextInput(attrs={'class': 'add-post', 'placeholder': 'eg. Newquay, Cornwall'}),
           'author': forms.TextInput(attrs={'class': 'add-post', 'value':'', 'id': 'userid', 'type': 'hidden' }),
           'body': forms.Textarea(attrs={'class': 'add-post' }),
        }

