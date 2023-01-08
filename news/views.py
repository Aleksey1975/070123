
from django.views.generic import ListView
from .models import News



class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news/news.html'
    context_object_name = 'news'