from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'   


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'  


