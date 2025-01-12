from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from blog.models import Post


class BlockListView(ListView):
    model = Post
    template_name = 'home.html'


# blog/views.py

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body', 'summary']
    success_url = reverse_lazy(
        'home')  # Muvaffaqiyatli yaratilgandan keyin qaysi sahifaga yo'naltirish kerakligini belgilang


def get_success_url(self):
    return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
