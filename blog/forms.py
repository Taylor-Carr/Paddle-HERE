from django import forms
from .models import Post, Comment

countries = [('England', 'England'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Northern Ireland', 'Northern Ireland'),]
sport = [('Surfing', 'Surfing'), ('Paddle Boarding', 'Paddle Boarding'), ('Kayaking', 'Kayaking'),]
proficiency_level = [('beginners', 'Beginners'),('intermediate', 'Intermediate'),('advanced', 'Advanced'),]
tags = [('', 'Select a tag for your post?'), ('free parking', 'Free Parking'), ('family friendly', 'Family Friendly'), ('no parking', 'No Parking'), ('pet friendly', 'Pet Friendly'),('wheelchair accessible', 'Wheelchair Accessible'),]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('location', 'country', 'category', 'tags', 'proficiency_level', 'body', 'post_image',)

        widgets = {
           'location': forms.TextInput(attrs={'class': 'add-post', 'placeholder': 'eg. Newquay, Cornwall'}),
           'country': forms.Select(attrs={'class': 'add-post' 'form-control'}, choices = countries,),
           'category': forms.Select(attrs={'class': 'add-post' 'form-control'}, choices = sport,),
           'proficiency_level': forms.Select(attrs={'class': 'add-post form-control'}, choices = proficiency_level,),
           'tags': forms.Select(attrs={'class': 'add-post form-control', 'placeholder': 'e.g. Free Parking..'}, choices = tags,),
           'post_image':forms.ClearableFileInput(attrs={'class': 'add-post form-control'}),
           'body': forms.Textarea(attrs={'class': 'post-body' 'add-post' }),
        }

        labels = {
            'body': 'Tell us about this spot:',
            'proficiency_level': 'Best for:',
            'post_image': 'Upload an image:',
            'category': 'Sport:',
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
        widgets = {'body': forms.Textarea(attrs={'class': 'add-post'}),}