from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'tasks/index.html')

def index(request):
    return render(request, 'tasks/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user).order_by('start_date')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


@login_required
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'tasks/task.html', context)


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks:tasks')


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task', task_id=task_id)
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)


@login_required
def new_task(request):
    if request.method != 'POST':
        form = TaskForm(initial={'assigner': request.user})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('tasks:tasks')
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)
