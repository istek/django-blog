from django.shortcuts import render
from django.views.generic import ListView
from .models import User, Post, Tag


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'allposts'

    def get_queryset(self):
        Post.objects.all("-post_time")
