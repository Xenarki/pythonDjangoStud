from django.shortcuts import render
import http

# Create your views here.
def news_home(request):
    return render(request, 'news/news_home.html')
