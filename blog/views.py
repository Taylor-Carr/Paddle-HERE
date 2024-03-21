from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_details', args=[str(pk)]))

def like_comment(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=pk)
        if comment.likes.filter(id=request.user.id):
            comment.likes.remove(request.user)
        
        else:
            comment.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    else:
        messages.success(request, ("You must be logged in to like a comment."))
        return redirect ('home')
  


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context



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

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateCommentView(UpdateView):
    model = Comment
    template_name= 'comment_update.html'
    fields = ['body']
    success_url = reverse_lazy('home')

class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')









