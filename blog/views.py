from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView)
from .models import Post
from django.urls import reverse_lazy


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


class EditBlog(UpdateView):
    model = Post
    template_name = 'edit_blog.html'
    fields = '__all__'


class DeleteBlog(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('blog')
