from django.urls import path
from .views import LandingPageView, HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing_page"),
    path('blog/', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog-details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('blog/edit/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
]