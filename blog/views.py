from django.views.generic import ListView
from .models import Post


# Create your views here.

class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'allposts'
    queryset = Post.objects.all().prefetch_related('user', 'tag')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
