from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'   


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html' 


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'location', 'body' ]


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



