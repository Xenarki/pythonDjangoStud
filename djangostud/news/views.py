from django.shortcuts import render
import http

# Create your views here.
def news_home(request):
    # return render(request, '1')
    return http.HttpResponse("My first mapped url")