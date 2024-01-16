from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context: dict = {
        "title" : 'Home',
        "content" : 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context)
    # return HttpResponse("<h4>Main Page</h4>")

