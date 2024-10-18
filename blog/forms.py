from django import forms
from .models import Post, Comment

countries = [('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Northern Ireland', 'Northern Ireland'),]
sport = [('Surfing', 'Surfing'), ('Paddle Boarding', 'Paddle Boarding'), ('Kayaking', 'Kayaking'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'country', 'location', 'body', 'post_image', 'tags', 'proficiency_level')

        widgets = {
           'title': forms.TextInput(attrs={'class': 'add-post' }),
           'location': forms.TextInput(attrs={'class': 'add-post', 'placeholder': 'eg. Newquay, Cornwall'}),
           'country': forms.Select(attrs={'class': 'add-post' 'form-control'}, choices = countries,),
           'category': forms.Select(attrs={'class': 'add-post' 'form-control'}, choices = sport,),
           'proficiency_level': forms.Select(attrs={'class': 'add-post form-control'}),
           'tags': forms.Select(attrs={'class': 'add-post form-control'}),
           'post_image':forms.ClearableFileInput(attrs={'class': 'add-post form-control'}),
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