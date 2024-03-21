from django import forms
from .models import Post, Comment

countries = [('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Northern Ireland', 'Northern Ireland'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'location','author', 'body')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'add-post' }),
           'location': forms.TextInput(attrs={'class': 'add-post', 'placeholder': 'eg. Newquay, Cornwall'}),
           'author': forms.TextInput(attrs={'class': 'add-post', 'value':'', 'id': 'userid', 'type': 'hidden' }),
           'category': forms.Select(attrs={'class': 'category' 'form-control'}, choices = countries,),
           'body': forms.Textarea(attrs={'class': 'post-body' 'add-post' }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
           'name': forms.TextInput(attrs={'class': 'add-post' }),
           'body': forms.Textarea(attrs={'class': 'add-post' }),
        }