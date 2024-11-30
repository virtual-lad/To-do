from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import logout
# from index.models import Task
# from index.forms import TaskForm


# def home(request):
#     tasks_list = Task.objects.order_by('-date')
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
        
#     else:
#         form = TaskForm()

#     data = {
#         'form':form,
#         'list':tasks_list,
#     }
#     return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form':form,
    })

def logout_view(request):
    logout(request)
    return redirect('index:home')

