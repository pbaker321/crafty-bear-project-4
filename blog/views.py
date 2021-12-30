from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog_details.html'


class AddBlog(CreateView):
    model = Post
    template_name = 'add_blog.html'
    fields = '__all__'
