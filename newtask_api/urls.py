from django.urls import path
from . import views
from .views import UserSignup, UserRegistationView

urlpatterns = [
    path('users/register/', UserRegistationView.as_view()),
    path('signup/', UserSignup.as_view()),
    path('users/', views.UserListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('like/', views.LikeCreateView.as_view()),
    path('dislike/', views.DisLikeCreateView.as_view()),
]


