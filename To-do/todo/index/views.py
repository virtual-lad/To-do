from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone


def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = []

    
    data_index = {
        'tasks':tasks,
    }
    return render(request, 'home.html', data_index)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index:home')
        
    else:
        form = TaskForm()

    data_add_task = {
        'form':form,
        }
    return render(request, 'add_task.html', data_add_task)

def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    clock = task.date
    done = task.is_completed

    return render(request, 'task_details.html', {
        'task':task,
        'clock':clock,
        'done':done
    })

def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=False)
            task.date = timezone.now()
            task.save()
            return redirect('index:home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_edit.html', {'form':form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index:home')
