from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from members.models import UserProfile


def profile_view(request):
    profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None
    return render(request, 'base.html', {'profile': profile})

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
        return redirect ('register')
  

def search_view(request):
    query = request.GET.get('q')
    results = Post.objects.all()

    if query:
        results = results.filter(
            Q(location__icontains=query) |
            Q(country__icontains=query) |
            Q(category__icontains=query) 
        )

    return render(request, 'search_results.html', {'results': results, 'query':query})



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
    def get_queryset(self):
        # Order posts by post_date in descending order
        return Post.objects.all().order_by('-post_date')


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        context["total_likes"] = total_likes
        context["post_image"] = post.post_image.url if post.post_image else None

        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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









