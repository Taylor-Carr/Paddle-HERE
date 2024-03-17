from django.urls import path
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, LikeCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog_details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('blog/edit/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('blog/like/<int:comment_pk>/', LikeCommentView, name="like_comment"),
]