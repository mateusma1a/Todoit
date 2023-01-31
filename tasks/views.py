from django.shortcuts import render, redirect
from tasks.models import Todo

# Create your views here.

def show_tasks(request):
    tasks = Todo.objects.order_by('title')
    context = {'tasks' : tasks}
    return render(request, "tasks/show_tasks.html", context)

def edit_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    if request.method == 'POST':
        form_data = request.POST
        task.title = form_data.get('title')
        task.text = form_data.get('text')
        task.done = form_data.get('done')
        task.save()
        return redirect("/tasks")
    else:
        return render(request, 'tasks/edit_task.html', {'task': task})
    
def new_task(request):
    if request.method == 'POST':
        form_data = request.POST
        task = Todo()
        task.title = form_data.get('title')
        task.text = form_data.get('text')
        task.save()
        return redirect("/tasks")
    else:
        return render(request, 'tasks/new_task.html')
    
def delete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect("/tasks")
    else:
        return render(request, 'tasks/delete_task.html', {'task': task})
