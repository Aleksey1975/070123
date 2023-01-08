from django.urls import path
# Импортируем созданное нами представление
from .views import *


urlpatterns = [
   path('', NewsList.as_view()),
]