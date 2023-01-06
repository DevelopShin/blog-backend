from django.shortcuts import render
from django.views.generic import DetailView

from post.models import Post


# Create your views here.
class PostDV(DetailView):
    model = Post
    templates_name = 'post/post_detail.html'
