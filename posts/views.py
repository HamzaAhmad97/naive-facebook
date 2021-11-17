from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['content', 'added_by']
    template_name = 'posts/posts_create.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')
    template_name = 'posts/posts_delete.html'