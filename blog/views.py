# Create your views here.
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView,UpdateView# new


from .models import Post


class BlogListView(ListView): 
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): # new model = Post
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    