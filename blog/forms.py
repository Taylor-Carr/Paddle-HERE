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
           'category': forms.Select(attrs={'class': 'add-post' 'form-control'}, choices = countries,),
           'body': forms.Textarea(attrs={'class': 'post-body' 'add-post' }),
        }


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CommentForm, self).save(commit=False)
        if self.user:
            instance.author = self.user
        if commit:
            instance.save()
        return instance 

    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
           'body': forms.Textarea(attrs={'class': 'add-post'}),
        }