from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

class PostListView(ListView):
    model = Post
    template_name = 'krnotes/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

    def get_queryset(self):
        user_query = self.request.GET.get('query')
        if not user_query:
            user_query = ''
        return Post.objects.filter(title__icontains=user_query).union(Post.objects.filter(content__icontains=user_query)).order_by('-date_posted')

class UserPostListView(ListView):
    model = Post
    template_name = 'krnotes/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class FoodPostListView(ListView):
    model = Post
    template_name = 'krnotes/food_posts.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(food=True).order_by('-date_posted')

class GardenPostListView(ListView):
    model = Post
    template_name = 'krnotes/garden_posts.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        return Post.objects.filter(garden=True).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'content', 'garden', 'food']
    success_url = '/krnotes'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'content', 'garden', 'food']
    success_url = '/krnotes'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/krnotes'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
