from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def tasks(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }

    return render(request, 'tasks.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')