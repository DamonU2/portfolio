from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    GardenPostListView,
    FoodPostListView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='krnotes-home'),
    path('food/', FoodPostListView.as_view(), name='krnotes-food'),
    path('garden/', GardenPostListView.as_view(), name='krnotes-garden'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]