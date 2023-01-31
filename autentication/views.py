from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'name': 'World'}
    return render(request, 'login.html', context)